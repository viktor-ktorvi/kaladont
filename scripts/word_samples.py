import random

from src.kaladont import LANGUAGES, _filter_words, detect_script, download_if_needed

SAMPLE_SIZE = 25


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

    print("| Language | Surviving words | Filtered out words |")
    print("|---|---|---|")
    for language, surviving, filtered_out in rows:
        surviving_str = ", ".join(f"*{w}*" for w in surviving)
        filtered_str = ", ".join(f"*{w}*" for w in filtered_out)
        print(f"| {language} | {surviving_str} | {filtered_str} |")


if __name__ == "__main__":
    main()
