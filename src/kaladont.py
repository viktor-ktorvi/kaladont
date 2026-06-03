import json
import random
import urllib.request
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

from wordfreq import zipf_frequency

Script = Literal[
    "latin",
    "cyrillic",
    "greek",
    "georgian",
    "armenian",
    "devanagari",
    "arabic",
    "bengali",
    "gurmukhi",
    "hangul",
    "hebrew",
]

CACHE_DIR = Path(__file__).parent.parent / "scripts"

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

VOWELS = set("aeiouáéíóúàèìòùâêîôûäëïöüýæœıøåyw")

EXCLUDE_SENSE_TAGS = {"abbreviation", "initialism", "acronym", "form-of", "alt-of"}

# Scripts that use combining/diacritic marks that aren't alpha — isalpha() fails on them
COMBINING_SCRIPTS: set[Script] = {"devanagari", "bengali", "gurmukhi", "arabic", "hebrew"}


@dataclass
class LanguageConfig:
    display_name: str
    folder_name: str  # folder segment in kaikki.org URL
    file_name: str  # filename base in kaikki.org URL
    script: Script | None  # None = accept all scripts
    wordfreq_lang: str  # language code for wordfreq
    min_frequency: float  # default Zipf frequency threshold (0 = disabled)
    allow_uppercase_start: bool = False  # some languages capitalize common nouns (e.g. German)
    min_word_size: int = 3  # minimum number of characters to keep a word
    chain_chars: int = 2  # characters taken from end/start for chaining


LANGUAGES: dict[str, LanguageConfig] = {
    # --- Indo-European ---
    # South Slavic
    "sh-latin": LanguageConfig("Serbo-Croatian (Latin)", "Serbo-Croatian", "SerboCroatian", "latin", "sh", 0.0),
    "sh-cyrillic": LanguageConfig(
        "Serbo-Croatian (Cyrillic)", "Serbo-Croatian", "SerboCroatian", "cyrillic", "sh", 0.0
    ),
    # "sl": LanguageConfig("Slovenian",  "Slovene",    "Slovene",    "latin",    "sl", 0.0),
    "mk": LanguageConfig("Macedonian", "Macedonian", "Macedonian", "cyrillic", "mk", 0.0),
    "bg": LanguageConfig("Bulgarian", "Bulgarian", "Bulgarian", "cyrillic", "bg", 0.0),
    # East Slavic
    "ru": LanguageConfig("Russian", "Russian", "Russian", "cyrillic", "ru", 2.0),
    "uk": LanguageConfig("Ukrainian", "Ukrainian", "Ukrainian", "cyrillic", "uk", 0.0),
    # "be": LanguageConfig("Belarusian", "Belarusian", "Belarusian", "cyrillic", "be", 0.0),
    # West Slavic
    "pl": LanguageConfig("Polish", "Polish", "Polish", "latin", "pl", 2.0),
    "cs": LanguageConfig("Czech", "Czech", "Czech", "latin", "cs", 2.0),
    "sk": LanguageConfig("Slovak", "Slovak", "Slovak", "latin", "sk", 0.0),
    # Baltic
    "lt": LanguageConfig("Lithuanian", "Lithuanian", "Lithuanian", "latin", "lt", 0.0),
    "lv": LanguageConfig("Latvian", "Latvian", "Latvian", "latin", "lv", 0.0),
    # Germanic
    "de": LanguageConfig("German", "German", "German", "latin", "de", 2.0, allow_uppercase_start=True),
    "en": LanguageConfig("English", "English", "English", "latin", "en", 2.0),
    "nl": LanguageConfig("Dutch", "Dutch", "Dutch", "latin", "nl", 2.0),
    "sv": LanguageConfig("Swedish", "Swedish", "Swedish", "latin", "sv", 2.0),
    # "no": LanguageConfig("Norwegian", "Norwegian", "Norwegian", "latin", "no", 0.0),
    # "da": LanguageConfig("Danish",    "Danish",    "Danish",    "latin", "da", 0.0),
    # "af": LanguageConfig("Afrikaans", "Afrikaans", "Afrikaans", "latin", "af", 0.0),
    # Romance
    "es": LanguageConfig("Spanish", "Spanish", "Spanish", "latin", "es", 2.0),
    "fr": LanguageConfig("French", "French", "French", "latin", "fr", 2.0),
    "it": LanguageConfig("Italian", "Italian", "Italian", "latin", "it", 2.0),
    "pt": LanguageConfig("Portuguese", "Portuguese", "Portuguese", "latin", "pt", 2.0),
    "ro": LanguageConfig("Romanian", "Romanian", "Romanian", "latin", "ro", 0.0),
    # "ca": LanguageConfig("Catalan",    "Catalan",    "Catalan",    "latin", "ca", 2.0),
    # "gl": LanguageConfig("Galician",   "Galician",   "Galician",   "latin", "gl", 0.0),
    # "oc": LanguageConfig("Occitan",    "Occitan",    "Occitan",    "latin", "oc", 0.0),
    # "la": LanguageConfig("Latin",      "Latin",      "Latin",      "latin", "la", 0.0),
    # Hellenic
    "el": LanguageConfig("Greek", "Greek", "Greek", "greek", "el", 0.0),
    # Armenian
    "hy": LanguageConfig("Armenian", "Armenian", "Armenian", "armenian", "hy", 0.0),
    # Celtic
    # "cy": LanguageConfig("Welsh", "Welsh", "Welsh", "latin", "cy", 0.0),
    # "ga": LanguageConfig("Irish", "Irish", "Irish", "latin", "ga", 0.0),
    # Albanian
    "sq": LanguageConfig("Albanian", "Albanian", "Albanian", "latin", "sq", 0.0),
    # Indo-Iranian
    "hi": LanguageConfig("Hindi", "Hindi", "Hindi", "devanagari", "hi", 0.0),
    # "ur": LanguageConfig("Urdu",     "Urdu",     "Urdu",     "arabic",     "ur", 0.0),
    "fa": LanguageConfig("Persian", "Persian", "Persian", "arabic", "fa", 0.0),
    # "bn": LanguageConfig("Bengali",  "Bengali",  "Bengali",  "bengali",    "bn", 0.0),
    # "pa": LanguageConfig("Punjabi",  "Punjabi",  "Punjabi",  "gurmukhi",   "pa", 0.0),
    # "mr": LanguageConfig("Marathi",  "Marathi",  "Marathi",  "devanagari", "mr", 0.0),
    # "ne": LanguageConfig("Nepali",   "Nepali",   "Nepali",   "devanagari", "ne", 0.0),
    # "sa": LanguageConfig("Sanskrit", "Sanskrit", "Sanskrit", "devanagari", "sa", 0.0),
    # --- Non-Indo-European ---
    # Kartvelian
    "ka": LanguageConfig("Georgian", "Georgian", "Georgian", "georgian", "ka", 0.0),
    # Uralic
    "fi": LanguageConfig("Finnish", "Finnish", "Finnish", "latin", "fi", 2.0),
    # Turkic
    "tr": LanguageConfig("Turkish", "Turkish", "Turkish", "latin", "tr", 0.0),
    # Koreanic
    "ko": LanguageConfig("Korean", "Korean", "Korean", "hangul", "ko", 0.0, min_word_size=2, chain_chars=1),
    # Austronesian
    "id": LanguageConfig("Indonesian", "Indonesian", "Indonesian", "latin", "id", 0.0),
    "ms": LanguageConfig("Malay", "Malay", "Malay", "latin", "ms", 0.0),
    # Semitic
    "ar": LanguageConfig("Arabic", "Arabic", "Arabic", "arabic", "ar", 0.0),
    # "he": LanguageConfig("Hebrew",  "Hebrew",  "Hebrew",  "hebrew", "he", 0.0),
    # Bantu
    "sw": LanguageConfig("Swahili", "Swahili", "Swahili", "latin", "sw", 0.0),
}


def is_clean_word(word: str, script: Script) -> bool:
    if script in COMBINING_SCRIPTS:
        return not any(c.isspace() or c.isdigit() or c in r".-_/\()[]{}" for c in word)
    return word.isalpha()


def has_vowel(word: str) -> bool:
    return any(c.lower() in VOWELS for c in word)


def has_excluded_sense_tag(entry: dict) -> bool:
    return any(not EXCLUDE_SENSE_TAGS.isdisjoint(sense.get("tags", [])) for sense in entry.get("senses", []))


def has_valid_casing(word: str, allow_uppercase_start: bool) -> bool:
    if word.islower():
        return True
    if not any(c.isupper() or c.islower() for c in word):
        return True  # caseless script (Devanagari, Arabic, etc.)
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
        if "ऀ" <= c <= "ॿ":
            return "devanagari"
        if "؀" <= c <= "ۿ":
            return "arabic"
        if "ঀ" <= c <= "৿":
            return "bengali"
        if "਀" <= c <= "੿":
            return "gurmukhi"
        if "가" <= c <= "힣":
            return "hangul"
        if "א" <= c <= "ת":
            return "hebrew"
    return "latin"


def download_if_needed(config: LanguageConfig) -> Path:
    cache_path = CACHE_DIR / f"{config.file_name}.jsonl"
    if not cache_path.exists():
        url = f"https://kaikki.org/dictionary/{config.folder_name}/" f"kaikki.org-dictionary-{config.file_name}.jsonl"
        print(f"Downloading {config.display_name} dictionary...")
        urllib.request.urlretrieve(url, cache_path)
        print("Done.")
    return cache_path


def _word_cache_path(config: LanguageConfig, min_frequency: float) -> Path:
    script_tag = config.script or "all"
    return CACHE_DIR / f"{config.file_name}-{script_tag}-{min_frequency}-{config.min_word_size}.txt"


def _filter_words(config: LanguageConfig, jsonl_path: Path, min_frequency: float) -> tuple[list[str], list[str]]:
    words: list[str] = []
    filtered: list[str] = []
    with open(jsonl_path) as f:
        for line in f:
            entry = json.loads(line)
            word = entry.get("word", "")
            if len(word) < config.min_word_size:
                continue
            word_script = detect_script(word)
            if (
                is_clean_word(word, word_script)
                and entry.get("pos") not in EXCLUDE_POS
                and has_valid_casing(word, config.allow_uppercase_start)
                and (config.script is None or word_script == config.script)
                and (word_script != "latin" or has_vowel(word))
                and not has_excluded_sense_tag(entry)
                and (min_frequency == 0.0 or zipf_frequency(word, config.wordfreq_lang) >= min_frequency)
            ):
                words.append(word)
            else:
                filtered.append(word)
    return list(dict.fromkeys(words)), list(dict.fromkeys(filtered))


def load_words(config: LanguageConfig, min_frequency: float) -> tuple[list[str], list[str]]:
    jsonl_path = download_if_needed(config)
    word_cache = _word_cache_path(config, min_frequency)

    if word_cache.exists() and word_cache.stat().st_mtime >= jsonl_path.stat().st_mtime:
        words = word_cache.read_text().splitlines()
        return words, []

    print("Building word list (this only happens once)...")
    words, filtered = _filter_words(config, jsonl_path, min_frequency)
    word_cache.write_text("\n".join(words))
    return words, filtered


def build_endings_map(words: list[str], chain_chars: int = 2) -> defaultdict[str, list[str]]:
    endings_map: defaultdict[str, list[str]] = defaultdict(list)
    for word in words:
        endings_map[word[:chain_chars]].append(word)
    return endings_map


def play_game(words: list[str], endings_map: defaultdict[str, list[str]], chain_chars: int = 2) -> list[str]:
    current_word = random.choice(words)
    used = [current_word]
    used_set = {current_word}
    while True:
        candidates = [w for w in endings_map[current_word[-chain_chars:]] if w not in used_set]
        if not candidates:
            break
        current_word = random.choice(candidates)
        used.append(current_word)
        used_set.add(current_word)
    return used


def sample(lst: list[str], k: int = 20) -> list[str]:
    return random.choices(lst, k=min(k, len(lst))) if lst else []
