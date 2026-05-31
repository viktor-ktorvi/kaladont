import json
import random
import urllib.request
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

from wordfreq import zipf_frequency

Script = Literal["latin", "cyrillic", "greek", "georgian", "armenian"]

CACHE_DIR = Path(__file__).parent.parent / "scripts"

EXCLUDE_POS = {
    "name", "suffix", "prefix", "character", "phrase", "proverb",
    "contraction", "interfix", "symbol", "infix", "combining_form",
}

VOWELS = set("aeiouáéíóúàèìòùâêîôûäëïöüýæœ")

ABBREVIATION_TAGS = {"abbreviation", "initialism", "acronym"}


@dataclass
class LanguageConfig:
    display_name: str
    folder_name: str        # folder segment in kaikki.org URL
    file_name: str          # filename base in kaikki.org URL
    script: Script | None   # None = accept all scripts
    wordfreq_lang: str      # language code for wordfreq
    min_frequency: float    # default Zipf frequency threshold (0 = disabled)
    allow_uppercase_start: bool = False  # German nouns are legitimately capitalized


LANGUAGES: dict[str, LanguageConfig] = {
    "sh-latin":    LanguageConfig("Serbo-Croatian (Latin)",    "Serbo-Croatian", "SerboCroatian", "latin",    "sh", 0.0),
    "sh-cyrillic": LanguageConfig("Serbo-Croatian (Cyrillic)", "Serbo-Croatian", "SerboCroatian", "cyrillic", "sh", 0.0),
    "de":          LanguageConfig("German",    "German",    "German",    "latin",    "de", 2.0, allow_uppercase_start=True),
    "en":          LanguageConfig("English",   "English",   "English",   "latin",    "en", 2.0),
    "es":          LanguageConfig("Spanish",   "Spanish",   "Spanish",   "latin",    "es", 2.0),
    "fr":          LanguageConfig("French",    "French",    "French",    "latin",    "fr", 2.0),
    "bg":          LanguageConfig("Bulgarian",  "Bulgarian",  "Bulgarian",  "cyrillic",  "bg", 0.0),
    "mk":          LanguageConfig("Macedonian", "Macedonian", "Macedonian", "cyrillic",  "mk", 0.0),
    "ru":          LanguageConfig("Russian",    "Russian",    "Russian",    "cyrillic",  "ru", 2.0),
    "uk":          LanguageConfig("Ukrainian",  "Ukrainian",  "Ukrainian",  "cyrillic",  "uk", 0.0),
    "el":          LanguageConfig("Greek",      "Greek",      "Greek",      "greek",     "el", 0.0),
    "hy":          LanguageConfig("Armenian",   "Armenian",   "Armenian",   "armenian",  "hy", 0.0),
    "ka":          LanguageConfig("Georgian",   "Georgian",   "Georgian",   "georgian",  "ka", 0.0),
    "it":          LanguageConfig("Italian",    "Italian",    "Italian",    "latin",     "it", 2.0),
    "pt":          LanguageConfig("Portuguese", "Portuguese", "Portuguese", "latin",     "pt", 2.0),
    "ro":          LanguageConfig("Romanian",   "Romanian",   "Romanian",   "latin",     "ro", 0.0),
    "nl":          LanguageConfig("Dutch",      "Dutch",      "Dutch",      "latin",     "nl", 2.0),
    "pl":          LanguageConfig("Polish",     "Polish",     "Polish",     "latin",     "pl", 2.0),
    "cs":          LanguageConfig("Czech",      "Czech",      "Czech",      "latin",     "cs", 2.0),
    "sq":          LanguageConfig("Albanian",   "Albanian",   "Albanian",   "latin",     "sq", 0.0),
    "sl":          LanguageConfig("Slovenian",  "Slovene",    "Slovene",    "latin",     "sl", 0.0),
}


def has_vowel(word: str) -> bool:
    return any(c.lower() in VOWELS for c in word)


def is_abbreviation(entry: dict) -> bool:
    return any(
        not ABBREVIATION_TAGS.isdisjoint(sense.get("tags", []))
        for sense in entry.get("senses", [])
    )


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
        if "Ա" <= c <= "ֆ":
            return "armenian"
    return "latin"


def download_if_needed(config: LanguageConfig) -> Path:
    cache_path = CACHE_DIR / f"{config.file_name}.jsonl"
    if not cache_path.exists():
        url = (
            f"https://kaikki.org/dictionary/{config.folder_name}/"
            f"kaikki.org-dictionary-{config.file_name}.jsonl"
        )
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


def build_endings_map(words: list[str]) -> defaultdict[str, list[str]]:
    endings_map: defaultdict[str, list[str]] = defaultdict(list)
    for word in words:
        endings_map[word[:2]].append(word)
    return endings_map


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
