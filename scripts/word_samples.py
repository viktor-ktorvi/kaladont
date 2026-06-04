import random

from src.kaladont import LANGUAGES, _filter_words, detect_script, download_if_needed

SAMPLE_SIZE = 25
LATEX_SAMPLE_SIZE = 10


def _latex_escape(word: str) -> str:
    for old, new in [("&", r"\&"), ("%", r"\%"), ("$", r"\$"), ("#", r"\#"), ("_", r"\_"), ("{", r"\{"), ("}", r"\}")]:
        word = word.replace(old, new)
    return word


def main() -> None:
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

    print("<table>")
    print("<tr><th>Language</th><th>Surviving words</th><th>Filtered out words</th></tr>")
    for language, surviving, filtered_out in rows:
        surviving_str = ", ".join(f"<em>{w}</em>" for w in surviving)
        filtered_str = ", ".join(f"<em>{w}</em>" for w in filtered_out)
        print(f"<tr><td>{language}</td><td>{surviving_str}</td><td>{filtered_str}</td></tr>")
    print("</table>")

    _print_latex_appendix(rows)


def _print_latex_appendix(rows: list[tuple]) -> None:
    print()
    print(r"\begin{longtable}{lp{5.5cm}p{5.5cm}}")
    print(r"\caption{Random sample of surviving and filtered-out words for each language.}")
    print(r"\label{tab:word-samples} \\")
    print(r"\toprule")
    print(r"Language & Surviving words & Filtered out words \\")
    print(r"\midrule")
    print(r"\endfirsthead")
    print(r"\multicolumn{3}{c}{\tablename\ \thetable\ -- continued} \\")
    print(r"\toprule")
    print(r"Language & Surviving words & Filtered out words \\")
    print(r"\midrule")
    print(r"\endhead")
    print(r"\midrule")
    print(r"\multicolumn{3}{r}{\textit{continued on next page}} \\")
    print(r"\endfoot")
    print(r"\bottomrule")
    print(r"\endlastfoot")
    for language, surviving, filtered_out in rows:
        surv = ", ".join(r"\textit{" + _latex_escape(w) + "}" for w in surviving[:LATEX_SAMPLE_SIZE])
        filt = ", ".join(r"\textit{" + _latex_escape(w) + "}" for w in filtered_out[:LATEX_SAMPLE_SIZE])
        print(f"{_latex_escape(language)} & {surv} & {filt} \\\\")
    print(r"\end{longtable}")


if __name__ == "__main__":
    main()
