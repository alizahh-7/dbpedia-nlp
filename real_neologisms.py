import json
import unicodedata

def normalize(word):
    return ''.join(
        c for c in unicodedata.normalize('NFD', word)
        if unicodedata.category(c) != 'Mn'
    )

print("Loading full vocabs...")
with open('freq_2026_full.json', 'r', encoding='utf-8') as f:
    freq_2026 = json.load(f)

with open('freq_2025_full.json', 'r', encoding='utf-8') as f:
    freq_2025 = json.load(f)

freq_2025_normalized = set(normalize(tok) for tok in freq_2025.keys())

neologisms = {
    tok: cnt for tok, cnt in freq_2026.items()
    if normalize(tok) not in freq_2025_normalized
    and cnt >= 3
    and tok.isalpha()
    and len(tok) >= 4
}

neologisms_sorted = sorted(neologisms.items(), key=lambda x: -x[1])

with open('neologisms_real.json', 'w', encoding='utf-8') as f:
    json.dump(neologisms_sorted[:5000], f, ensure_ascii=False, indent=2)

print(f"Total REAL neologisms: {len(neologisms_sorted)}")
print("Top 20:")
for word, count in neologisms_sorted[:20]:
    print(f"  {word}: {count}")
