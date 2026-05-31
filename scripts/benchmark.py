import argparse
import csv
import statistics
from datetime import datetime
from pathlib import Path

from src.kaladont import LANGUAGES, build_endings_map, load_words, play_game


def benchmark_language(
    lang_key: str,
    n_simulations: int,
    min_word_size: int,
) -> dict:
    config = LANGUAGES[lang_key]
    words, filtered = load_words(config, config.min_frequency, min_word_size)

    row = {
        "language_key": lang_key,
        "language": config.display_name,
        "script": config.script or "any",
        "min_frequency": config.min_frequency,
        "min_word_size": min_word_size,
        "num_words": len(words),
        "num_filtered": len(filtered) if filtered else "cached",
    }

    if not words:
        row.update({"game_min": None, "game_max": None, "game_mean": None, "game_median": None, "game_std": None})
        return row

    endings_map = build_endings_map(words)
    game_lengths = [len(play_game(words, endings_map)) for _ in range(n_simulations)]

    row.update(
        {
            "game_min": min(game_lengths),
            "game_max": max(game_lengths),
            "game_mean": round(statistics.mean(game_lengths), 1),
            "game_median": statistics.median(game_lengths),
            "game_std": round(statistics.stdev(game_lengths), 1),
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
        "--min-word-size",
        "-w",
        type=int,
        default=4,
        help="Minimum word length in characters (default: 4)",
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
            row = benchmark_language(lang_key, args.simulations, args.min_word_size)
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

    fieldnames = [
        "language_key",
        "language",
        "script",
        "min_frequency",
        "min_word_size",
        "num_words",
        "num_filtered",
        "game_min",
        "game_max",
        "game_mean",
        "game_median",
        "game_std",
    ]
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    _print_table(rows, fieldnames)
    print(f"\nResults written to {output_path}")


def _print_table(rows: list[dict], columns: list[str]) -> None:
    str_rows = [{c: str(row.get(c, "")) for c in columns} for row in rows]
    widths = {c: max(len(c), max(len(r[c]) for r in str_rows)) for c in columns}

    sep = f"+-{'-+-'.join(('-' * widths[c] for c in columns))}-+"
    header = f"| {' | '.join((c.ljust(widths[c]) for c in columns))} |"

    print(f"\n{sep}\n{header}\n{sep}")
    for row in str_rows:
        print(f"| {' | '.join((row[c].ljust(widths[c]) for c in columns))} |")
    print(sep)


if __name__ == "__main__":
    main()
