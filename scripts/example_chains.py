import argparse
import io
from pathlib import Path

from src.kaladont import LANGUAGES, build_endings_map, load_words, play_game

N_CHAINS = 5
MIN_LEN = 3
MAX_LEN = 8
MAX_ATTEMPTS = 3000

PAPER_DIR = Path(__file__).parent.parent / "paper"


def _collect_lang(lang_key: str) -> tuple[str, list[list[str]]]:
    config = LANGUAGES[lang_key]
    words, _ = load_words(config, config.min_frequency)
    if not words:
        return config.display_name, []
    endings_map = build_endings_map(words, config.chain_chars)
    chains: list[list[str]] = []
    for _ in range(MAX_ATTEMPTS):
        if len(chains) >= N_CHAINS:
            break
        game = play_game(words, endings_map, config.chain_chars)
        if MIN_LEN <= len(game) <= MAX_LEN:
            chains.append(game)
    return config.display_name, chains


def collect_data() -> list[tuple[str, list[list[str]]]]:
    data = []
    for lang_key in LANGUAGES:
        print(f"  [{lang_key}]", end=" ", flush=True)
        data.append(_collect_lang(lang_key))
    print()
    return data


def _arrow_join(chain: list[str]) -> str:
    return " → ".join(chain)


def build_html_table(data: list[tuple[str, list[list[str]]]]) -> str:
    buf = io.StringIO()
    buf.write("<table>\n")
    buf.write("<tr><th>Language</th><th>Example chain</th></tr>\n")
    for lang, chains in data:
        if not chains:
            buf.write(f"<tr><td>{lang}</td><td>—</td></tr>\n")
            continue
        for i, chain in enumerate(chains):
            label = lang if i == 0 else ""
            buf.write(f"<tr><td>{label}</td><td>{_arrow_join(chain)}</td></tr>\n")
    buf.write("</table>")
    return buf.getvalue()


def build_latex_table(data: list[tuple[str, list[list[str]]]]) -> str:
    buf = io.StringIO()
    w = buf.write
    w(r"\begin{longtable}{lp{10cm}}\n")
    w(r"\caption{Example game chains (3--8 words each).}\n")
    w(r"\label{tab:example-chains} \\\n")
    w(r"\toprule\n")
    w(r"Language & Example chain \\\n")
    w(r"\midrule\n")
    w(r"\endfirsthead\n")
    w(r"\multicolumn{2}{c}{\tablename\ \thetable\ -- continued} \\\n")
    w(r"\toprule\n")
    w(r"Language & Example chain \\\n")
    w(r"\midrule\n")
    w(r"\endhead\n")
    w(r"\midrule\n")
    w(r"\multicolumn{2}{r}{\textit{continued on next page}} \\\n")
    w(r"\endfoot\n")
    w(r"\bottomrule\n")
    w(r"\endlastfoot\n")
    for idx, (lang, chains) in enumerate(data):
        if idx > 0:
            buf.write(r"\midrule\n")
        if not chains:
            buf.write(f"{lang} & --- \\\\\n")
            continue
        for i, chain in enumerate(chains):
            label = lang if i == 0 else ""
            chain_latex = r" $\rightarrow$ ".join(chain)
            buf.write(f"{label} & {chain_latex} \\\\\n")
    w(r"\end{longtable}\n")
    return buf.getvalue()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=None, help="Random seed for reproducible chains")
    parser.add_argument("--write", action="store_true", help="Write LaTeX table to paper/example_chains_table.tex")
    args = parser.parse_args()

    if args.seed is not None:
        import random

        random.seed(args.seed)

    data = collect_data()
    print(build_html_table(data))

    latex = build_latex_table(data)
    if args.write:
        out = PAPER_DIR / "example_chains_table.tex"
        out.write_text(latex, encoding="utf-8")
        print(f"\nWrote {out}")
    else:
        print(latex)


if __name__ == "__main__":
    main()
