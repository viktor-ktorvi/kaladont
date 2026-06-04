import argparse
import io
import random
from pathlib import Path

from src.kaladont import LANGUAGES, _filter_words, detect_script, download_if_needed

SAMPLE_SIZE = 25
LATEX_SAMPLE_SIZE = 10

PAPER_DIR = Path(__file__).parent.parent / "paper"


def _latex_escape(word: str) -> str:
    for old, new in [("&", r"\&"), ("%", r"\%"), ("$", r"\$"), ("#", r"\#"), ("_", r"\_"), ("{", r"\{"), ("}", r"\}")]:
        word = word.replace(old, new)
    return word


def collect_rows() -> list[tuple]:
    rows = []
    for lang_key, config in LANGUAGES.items():
        jsonl_path = download_if_needed(config)
        words, filtered = _filter_words(config, jsonl_path, config.min_frequency)
        words = list(dict.fromkeys(words))
        filtered = list(dict.fromkeys(filtered))
        if config.script is not None:
            filtered = [w for w in filtered if detect_script(w) == config.script]
        surviving_sample = random.sample(words, min(SAMPLE_SIZE, len(words)))
        filtered_sample = random.sample(filtered, min(SAMPLE_SIZE, len(filtered)))
        rows.append((config.display_name, surviving_sample, filtered_sample))
    return rows


def build_html_table(rows: list[tuple]) -> str:
    buf = io.StringIO()
    buf.write("<table>\n")
    buf.write("<tr><th>Language</th><th>Surviving words</th><th>Filtered out words</th></tr>\n")
    for language, surviving, filtered_out in rows:
        surviving_str = ", ".join(f"<em>{w}</em>" for w in surviving)
        filtered_str = ", ".join(f"<em>{w}</em>" for w in filtered_out)
        buf.write(f"<tr><td>{language}</td><td>{surviving_str}</td><td>{filtered_str}</td></tr>\n")
    buf.write("</table>")
    return buf.getvalue()


def build_latex_table(rows: list[tuple]) -> str:
    buf = io.StringIO()
    w = buf.write
    w(r"\begin{longtable}{lp{5.5cm}p{5.5cm}}" + "\n")
    w(r"\caption{Random sample of surviving and filtered-out words for each language.}" + "\n")
    w(r"\label{tab:word-samples} \\" + "\n")
    w(r"\toprule" + "\n")
    w(r"Language & Surviving words & Filtered out words \\" + "\n")
    w(r"\midrule" + "\n")
    w(r"\endfirsthead" + "\n")
    w(r"\multicolumn{3}{c}{\tablename\ \thetable\ -- continued} \\" + "\n")
    w(r"\toprule" + "\n")
    w(r"Language & Surviving words & Filtered out words \\" + "\n")
    w(r"\midrule" + "\n")
    w(r"\endhead" + "\n")
    w(r"\midrule" + "\n")
    w(r"\multicolumn{3}{r}{\textit{continued on next page}} \\" + "\n")
    w(r"\endfoot" + "\n")
    w(r"\bottomrule" + "\n")
    w(r"\endlastfoot" + "\n")
    for language, surviving, filtered_out in rows:
        surv = ", ".join(_latex_escape(word) for word in surviving[:LATEX_SAMPLE_SIZE])
        filt = ", ".join(_latex_escape(word) for word in filtered_out[:LATEX_SAMPLE_SIZE])
        buf.write(f"{_latex_escape(language)} & {surv} & {filt} \\\\\n")
    w(r"\end{longtable}" + "\n")
    return buf.getvalue()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=None, help="Random seed for reproducible samples")
    parser.add_argument("--write", action="store_true", help="Write LaTeX table to paper/word_samples_table.tex")
    args = parser.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    rows = collect_rows()

    print(build_html_table(rows))
    latex = build_latex_table(rows)
    if args.write:
        out = PAPER_DIR / "word_samples_table.tex"
        out.write_text(latex, encoding="utf-8")
        print(f"\nWrote {out}")
    else:
        print(latex)


if __name__ == "__main__":
    main()
