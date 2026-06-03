import argparse
import statistics

from src.kaladont import (
    LANGUAGES,
    build_endings_map,
    detect_script,
    load_words,
    play_game,
    sample,
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Kaladont word chain game")
    parser.add_argument(
        "--language",
        "-l",
        choices=list(LANGUAGES),
        default="sh-latin",
        help="Language to play in (default: sh-latin)",
    )
    parser.add_argument(
        "--simulations",
        "-n",
        type=int,
        default=100,
        help="Number of Monte Carlo simulations (default: 100)",
    )
    parser.add_argument(
        "--min-frequency",
        "-f",
        type=float,
        default=None,
        help="Minimum Zipf frequency to include a word (0=off, 3=once per million words, default: per-language)",
    )
    args = parser.parse_args()

    config = LANGUAGES[args.language]
    min_frequency = args.min_frequency if args.min_frequency is not None else config.min_frequency
    print(f"Language: {config.display_name}")
    print(f"Min frequency (Zipf): {min_frequency}")

    words, filtered = load_words(config, min_frequency)
    filtered_sample = [w for w in filtered if detect_script(w) == config.script] if config.script else filtered
    print(f"Loaded {len(words)} words, e.g.:    {sample(words)}")
    print(f"Filtered {len(filtered)} words, e.g.: {sample(filtered_sample)}")

    if not words:
        print("No words loaded — cannot run simulations.")
        return

    endings_map = build_endings_map(words, config.chain_chars)

    last_game: list[str] = []
    game_lengths: list[int] = []
    for _ in range(args.simulations):
        last_game = play_game(words, endings_map, config.chain_chars)
        game_lengths.append(len(last_game))

    print(f"\nGame lengths over {args.simulations} simulations:")
    print(f"  Min:    {min(game_lengths)}")
    print(f"  Max:    {max(game_lengths)}")
    print(f"  Mean:   {statistics.mean(game_lengths):.1f}")
    print(f"  Median: {statistics.median(game_lengths)}")
    print(f"  Std:    {statistics.stdev(game_lengths):.1f}")
    print(f"\nLast game ({len(last_game)} words):\n{' -> '.join(last_game)}")


if __name__ == "__main__":
    main()
