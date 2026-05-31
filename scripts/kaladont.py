import argparse
import json
import random
import statistics
import urllib.request
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

from wordfreq import zipf_frequency

Script = Literal["latin", "cyrillic", "greek", "georgian"]

CACHE_DIR = Path(__file__).parent

EXCLUDE_POS = {
    "name",
    "suffix",
    "prefix",
    "character",
    "phrase",
    "proverb",
    "contraction",
    "interfix",
    "symbol",
    "infix",
    "combining_form",
}

VOWELS = set("aeiouáéíóúàèìòùâêîôûäëïöüýæœ")

ABBREVIATION_TAGS = {"abbreviation", "initialism", "acronym"}


@dataclass
class LanguageConfig:
    display_name: str
    folder_name: str  # folder segment in kaikki.org URL
    file_name: str  # filename base in kaikki.org URL
    script: Script | None  # None = accept all scripts
    wordfreq_lang: str  # language code for wordfreq
    min_frequency: float  # default Zipf frequency threshold (0 = disabled)
    allow_uppercase_start: bool = False  # German nouns are legitimately capitalized


LANGUAGES: dict[str, LanguageConfig] = {
    "sh-latin": LanguageConfig("Serbo-Croatian (Latin)", "Serbo-Croatian", "SerboCroatian", "latin", "sh", 0.0),
    "sh-cyrillic": LanguageConfig(
        "Serbo-Croatian (Cyrillic)", "Serbo-Croatian", "SerboCroatian", "cyrillic", "sh", 0.0
    ),
    "de": LanguageConfig("German", "German", "German", "latin", "de", 2.0, allow_uppercase_start=True),
    "en": LanguageConfig("English", "English", "English", "latin", "en", 2.0),
    "es": LanguageConfig("Spanish", "Spanish", "Spanish", "latin", "es", 2.0),
    "fr": LanguageConfig("French", "French", "French", "latin", "fr", 2.0),
    "bg": LanguageConfig("Bulgarian", "Bulgarian", "Bulgarian", "cyrillic", "bg", 0.0),
    "el": LanguageConfig("Greek", "Greek", "Greek", "greek", "el", 0.0),
    "ka": LanguageConfig("Georgian", "Georgian", "Georgian", "georgian", "ka", 0.0),
    "sl": LanguageConfig("Slovenian", "Slovenian", "Slovenian", "latin", "sl", 0.0),
}


def has_vowel(word: str) -> bool:
    return any(c.lower() in VOWELS for c in word)


def is_abbreviation(entry: dict) -> bool:
    return any(not ABBREVIATION_TAGS.isdisjoint(sense.get("tags", [])) for sense in entry.get("senses", []))


def has_valid_casing(word: str, allow_uppercase_start: bool) -> bool:
    if word.islower():
        return True
    if allow_uppercase_start and word[0].isupper() and word[1:].islower():
        return True
    return False


def detect_script(word: str) -> Script:
    for c in word:
        if "Ѐ" <= c <= "ӿ":
            return "cyrillic"
        if "Ͱ" <= c <= "Ͽ":
            return "greek"
        if "ა" <= c <= "ჿ":
            return "georgian"
    return "latin"


def download_if_needed(config: LanguageConfig) -> Path:
    cache_path = CACHE_DIR / f"{config.file_name}.jsonl"
    if not cache_path.exists():
        url = f"https://kaikki.org/dictionary/{config.folder_name}/" f"kaikki.org-dictionary-{config.file_name}.jsonl"
        print(f"Downloading {config.display_name} dictionary...")
        urllib.request.urlretrieve(url, cache_path)
        print("Done.")
    return cache_path


def _word_cache_path(config: LanguageConfig, min_frequency: float, min_word_size: int) -> Path:
    script_tag = config.script or "all"
    return CACHE_DIR / f"{config.file_name}-{script_tag}-{min_frequency}-{min_word_size}.txt"


def _filter_words(
    config: LanguageConfig, jsonl_path: Path, min_frequency: float, min_word_size: int
) -> tuple[list[str], list[str]]:
    words: list[str] = []
    filtered: list[str] = []
    with open(jsonl_path) as f:
        for line in f:
            entry = json.loads(line)
            word = entry.get("word", "")
            if len(word) < min_word_size:
                continue
            word_script = detect_script(word)
            if (
                word.isalpha()
                and entry.get("pos") not in EXCLUDE_POS
                and has_valid_casing(word, config.allow_uppercase_start)
                and (config.script is None or word_script == config.script)
                and (word_script != "latin" or has_vowel(word))
                and not is_abbreviation(entry)
                and (min_frequency == 0.0 or zipf_frequency(word, config.wordfreq_lang) >= min_frequency)
            ):
                words.append(word)
            else:
                filtered.append(word)
    return list(dict.fromkeys(words)), list(dict.fromkeys(filtered))


def load_words(config: LanguageConfig, min_frequency: float, min_word_size: int) -> tuple[list[str], list[str]]:
    jsonl_path = download_if_needed(config)
    word_cache = _word_cache_path(config, min_frequency, min_word_size)

    if word_cache.exists() and word_cache.stat().st_mtime >= jsonl_path.stat().st_mtime:
        words = word_cache.read_text().splitlines()
        return words, []

    print("Building word list (this only happens once)...")
    words, filtered = _filter_words(config, jsonl_path, min_frequency, min_word_size)
    word_cache.write_text("\n".join(words))
    return words, filtered


def play_game(words: list[str], endings_map: defaultdict[str, list[str]]) -> list[str]:
    current_word = random.choice(words)
    used = [current_word]
    used_set = {current_word}
    while True:
        candidates = [w for w in endings_map[current_word[-2:]] if w not in used_set]
        if not candidates:
            break
        current_word = random.choice(candidates)
        used.append(current_word)
        used_set.add(current_word)
    return used


def sample(lst: list[str], k: int = 20) -> list[str]:
    return random.choices(lst, k=min(k, len(lst))) if lst else []


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
    parser.add_argument(
        "--min-word-size",
        "-w",
        type=int,
        default=4,
        help="Minimum word length in characters (default: 4)",
    )
    args = parser.parse_args()

    config = LANGUAGES[args.language]
    min_frequency = args.min_frequency if args.min_frequency is not None else config.min_frequency
    print(f"Language: {config.display_name}")
    print(f"Min frequency (Zipf): {min_frequency}")

    words, filtered = load_words(config, min_frequency, args.min_word_size)
    filtered_sample = [w for w in filtered if detect_script(w) == config.script] if config.script else filtered
    print(f"Loaded {len(words)} words, e.g.:    {sample(words)}")
    print(f"Filtered {len(filtered)} words, e.g.: {sample(filtered_sample)}")

    if not words:
        print("No words loaded — cannot run simulations.")
        return

    endings_map: defaultdict[str, list[str]] = defaultdict(list)
    for word in words:
        endings_map[word[:2]].append(word)

    last_game: list[str] = []
    game_lengths: list[int] = []
    for _ in range(args.simulations):
        last_game = play_game(words, endings_map)
        game_lengths.append(len(last_game))

    print(f"\nGame lengths over {args.simulations} simulations:")
    print(f"  Min:    {min(game_lengths)}")
    print(f"  Max:    {max(game_lengths)}")
    print(f"  Mean:   {statistics.mean(game_lengths):.1f}")
    print(f"  Median: {statistics.median(game_lengths)}")
    print(f"  Std:    {statistics.stdev(game_lengths):.1f}")
    print(f"\nLast game: {' -> '.join(last_game[:10])} ...")


if __name__ == "__main__":
    main()
