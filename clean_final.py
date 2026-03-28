import json
import unicodedata
import re

def normalize(word):
    return ''.join(
        c for c in unicodedata.normalize('NFD', word)
        if unicodedata.category(c) != 'Mn'
    )

def is_real_word(word):
    # Remove hex colors, codes, mixed garbage
    if re.search(r'[0-9]', word):           return False
    if re.search(r'[a-f]{4,}', word):       return False  # hex-like
    if len(word) < 5:                        return False
    if len(word) > 25:                       return False
    # Must have vowels (real Spanish words have vowels)
    if not re.search(r'[aeiouáéíóúü]', word): return False
    # No repeating 3+ same chars
    if re.search(r'(.)\1{2,}', word):       return False
    return True

print("Loading...")
with open('freq_2026_full.json', 'r', encoding='utf-8') as f:
    freq_2026 = json.load(f)
with open('freq_2025_full.json', 'r', encoding='utf-8') as f:
    freq_2025 = json.load(f)

freq_2025_normalized = set(normalize(tok) for tok in freq_2025.keys())

neologisms = {
    tok: cnt for tok, cnt in freq_2026.items()
    if normalize(tok) not in freq_2025_normalized
    and cnt >= 10
    and tok.isalpha()
    and is_real_word(tok)
}

neologisms_sorted = sorted(neologisms.items(), key=lambda x: -x[1])

with open('neologisms_clean_final.json', 'w', encoding='utf-8') as f:
    json.dump(neologisms_sorted[:5000], f, ensure_ascii=False, indent=2)

print(f"Total clean neologisms: {len(neologisms_sorted)}")
print("Top 30:")
for word, count in neologisms_sorted[:30]:
    print(f"  {word}: {count}")
