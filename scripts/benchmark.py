import argparse
import csv
import statistics
from datetime import datetime
from pathlib import Path

from src.kaladont import LANGUAGES, build_endings_map, load_words, play_game


def benchmark_language(lang_key: str, n_simulations: int) -> dict:
    config = LANGUAGES[lang_key]
    words, filtered = load_words(config, config.min_frequency)

    row = {
        "language_key": lang_key,
        "language": config.display_name,
        "script": config.script or "any",
        "min_frequency": config.min_frequency,
        "min_word_size": config.min_word_size,
        "chain_chars": config.chain_chars,
        "num_words": len(words),
        "num_filtered": len(filtered) if filtered else "cached",
    }

    if not words:
        row.update(
            {
                "game_min": None,
                "game_max": None,
                "game_mean": None,
                "game_median": None,
                "game_std": None,
                "example_chain": "",
            }
        )
        return row

    endings_map = build_endings_map(words, config.chain_chars)
    games = [play_game(words, endings_map, config.chain_chars) for _ in range(n_simulations)]
    game_lengths = [len(g) for g in games]

    good = [g for g in games if 3 <= len(g) <= 10]
    example = good[0] if good else min(games, key=lambda g: abs(len(g) - 6))

    row.update(
        {
            "game_min": min(game_lengths),
            "game_max": max(game_lengths),
            "game_mean": round(statistics.mean(game_lengths), 1),
            "game_median": statistics.median(game_lengths),
            "game_std": round(statistics.stdev(game_lengths), 1),
            "example_chain": " → ".join(example),
        }
    )
    return row


def main() -> None:
    parser = argparse.ArgumentParser(description="Benchmark kaladont across all languages")
    parser.add_argument(
        "--simulations",
        "-n",
        type=int,
        default=100,
        help="Number of Monte Carlo simulations per language (default: 100)",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        default=None,
        help="Output CSV path (default: benchmark_YYYYMMDD_HHMMSS.csv)",
    )
    args = parser.parse_args()

    output_path = args.output or Path(f"benchmark_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")

    rows = []
    for lang_key in LANGUAGES:
        print(f"\n[{lang_key}] {LANGUAGES[lang_key].display_name}")
        try:
            row = benchmark_language(lang_key, args.simulations)
        except Exception as e:
            print(f"  ERROR: {e}")
            row = {"language_key": lang_key, "language": LANGUAGES[lang_key].display_name, "error": str(e)}
        else:
            print(
                f"  words={row['num_words']}  filtered={row['num_filtered']}"
                f"  mean={row['game_mean']}  std={row['game_std']}"
                f"  min={row['game_min']}  max={row['game_max']}"
            )
        rows.append(row)

    csv_fieldnames = [
        "language_key",
        "language",
        "script",
        "min_frequency",
        "min_word_size",
        "chain_chars",
        "num_words",
        "num_filtered",
        "game_min",
        "game_max",
        "game_mean",
        "game_median",
        "game_std",
    ]
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=csv_fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    rows_sorted = sorted(rows, key=lambda r: r.get("game_mean") or 0, reverse=True)

    display_columns = [
        "language",
        "min_frequency",
        "min_word_size",
        "chain_chars",
        "num_words",
        "game_max",
        "game_mean",
        "game_median",
        "example_chain",
    ]
    _print_markdown_table(rows_sorted, display_columns)
    _print_ascii_table(rows_sorted, display_columns)
    _print_latex_table(rows_sorted, [c for c in display_columns if c != "example_chain"])

    print(f"\nResults written to {output_path}")


_COLUMN_HEADERS = {
    "language": "Language",
    "min_frequency": "Min Freq",
    "min_word_size": "Min Len",
    "chain_chars": "Overlap",
    "num_words": "Words",
    "game_min": "Min",
    "game_max": "Max",
    "game_mean": "Mean",
    "game_median": "Median",
    "game_std": "Std",
    "example_chain": "Example chain",
}


def _fmt_cell(col: str, val: object) -> str:
    if val is None or val == "":
        return ""
    s = str(val)
    if col == "min_frequency":
        return "—" if float(s) == 0.0 else s
    if col == "num_words":
        return f"{int(s):,}"
    return s


def _print_markdown_table(rows: list[dict], columns: list[str]) -> None:
    headers = "".join(f"<th>{_COLUMN_HEADERS.get(c, c)}</th>" for c in columns)
    print("\n<table>")
    print(f"<tr>{headers}</tr>")
    for row in rows:
        cells = "".join(f"<td>{_fmt_cell(c, row.get(c, ''))}</td>" for c in columns)
        print(f"<tr>{cells}</tr>")
    print("</table>")


def _print_ascii_table(rows: list[dict], columns: list[str]) -> None:
    header_labels = {c: _COLUMN_HEADERS.get(c, c) for c in columns}
    str_rows = [{c: _fmt_cell(c, row.get(c, "")) for c in columns} for row in rows]
    widths = {c: max(len(header_labels[c]), max(len(r[c]) for r in str_rows)) for c in columns}

    sep = f"+-{'-+-'.join('-' * widths[c] for c in columns)}-+"
    header = f"| {' | '.join(header_labels[c].ljust(widths[c]) for c in columns)} |"

    print(f"\n{sep}\n{header}\n{sep}")
    for row in str_rows:
        print(f"| {' | '.join(row[c].ljust(widths[c]) for c in columns)} |")
    print(sep)


def _print_latex_table(rows: list[dict], columns: list[str]) -> None:
    _NUMERIC = {
        "num_words",
        "game_min",
        "game_max",
        "game_mean",
        "game_median",
        "game_std",
        "chain_chars",
        "min_word_size",
        "min_frequency",
    }
    alignment = "".join("r" if c in _NUMERIC else "l" for c in columns)

    def _fmt_latex(col: str, val: object) -> str:
        if val is None or val == "":
            return ""
        s = str(val)
        if col == "min_frequency":
            return r"\textemdash" if float(s) == 0.0 else s
        if col == "num_words":
            return f"{int(s):,}".replace(",", "{,}")
        return s

    print()
    print(r"\begin{table}[h]")
    print(r"\centering")
    print(r"\caption{Chain length statistics (1000 simulations each).}")
    print(r"\label{tab:results}")
    print(f"\\begin{{tabular}}{{{alignment}}}")
    print(r"\toprule")
    print(" & ".join(_COLUMN_HEADERS.get(c, c) for c in columns) + r" \\")
    print(r"\midrule")
    for row in rows:
        print(" & ".join(_fmt_latex(c, row.get(c, "")) for c in columns) + r" \\")
    print(r"\bottomrule")
    print(r"\end{tabular}")
    print(r"\end{table}")


if __name__ == "__main__":
    main()
