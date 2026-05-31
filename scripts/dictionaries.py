import json
import random
import statistics
import urllib.request
from collections import defaultdict
from pathlib import Path

JSONL_URL = "https://kaikki.org/dictionary/Serbo-Croatian/kaikki.org-dictionary-SerboCroatian.jsonl"
CACHE_PATH = Path(__file__).parent / "serbo-croatian.jsonl"

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


def script(word: str) -> str:
    if any("Ѐ" <= c <= "ӿ" for c in word):
        return "cyrillic"
    return "latin"


def main() -> None:
    if not CACHE_PATH.exists():
        print("Downloading Serbo-Croatian dictionary...")
        urllib.request.urlretrieve(JSONL_URL, CACHE_PATH)
        print("Done.")

    legit_words = []
    filtered_words = []
    with open(CACHE_PATH) as f:
        for line in f:
            entry = json.loads(line)
            word = entry.get("word", "")
            if len(word) >= 3 and word[0].islower() and entry.get("pos") not in EXCLUDE_POS:
                legit_words.append(word)
            elif len(word) >= 3:
                filtered_words.append(word)

    legit_words = list(dict.fromkeys(legit_words))  # deduplicate, preserve order
    filtered_words = list(dict.fromkeys(filtered_words))

    cyrillic_words = [w for w in legit_words if script(w) == "cyrillic"]
    latin_words = [w for w in legit_words if script(w) == "latin"]

    legit_words = latin_words

    print(f"Retrieved {len(legit_words)} Serbo-Croatian lemmas")
    print(f"  Cyrillic: {len(cyrillic_words)}")
    print(f"  Latin:    {len(latin_words)}")
    print(f"Filtered out {len(filtered_words)} words, e.g.: {random.choices(filtered_words, k=20)}")
    print(f"Kept {len(legit_words)} words, e.g.: {random.choices(legit_words, k=20)}")

    endings_to_new_words = defaultdict(list)
    for word in legit_words:
        endings_to_new_words[word[:2]].append(word)

    # kaladont
    used_words = []
    game_lengths = []
    for i in range(100):
        current_word = random.choice(legit_words)
        used_words = [current_word]

        while True:
            ending = current_word[-2:]
            candidates = [w for w in endings_to_new_words[ending] if w not in used_words]
            if not candidates:
                break
            current_word = random.choice(candidates)
            used_words.append(current_word)

        game_lengths.append(len(used_words))

    print(f"Game lengths over {len(game_lengths)} simulations:")
    print(f"  Min:    {min(game_lengths)}")
    print(f"  Max:    {max(game_lengths)}")
    print(f"  Mean:   {statistics.mean(game_lengths):.1f}")
    print(f"  Median: {statistics.median(game_lengths)}")
    print(f"  Std:    {statistics.stdev(game_lengths):.1f}")
    print(" -> ".join(used_words[:10]), "...")


if __name__ == "__main__":
    main()
