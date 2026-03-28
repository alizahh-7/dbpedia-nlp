import json
import unicodedata

def normalize(word):
    # Remove accents for comparison
    return ''.join(
        c for c in unicodedata.normalize('NFD', word)
        if unicodedata.category(c) != 'Mn'
    )

with open('freq_2026.json', 'r', encoding='utf-8') as f:
    freq_2026 = json.load(f)

with open('freq_2025.json', 'r', encoding='utf-8') as f:
    freq_2025 = json.load(f)

# Normalize 2025 tokens for comparison
freq_2025_normalized = set(normalize(tok) for tok in freq_2025.keys())

# Neologisms = 2026 words whose normalized form is NOT in 2025
neologisms = {
    tok: cnt for tok, cnt in freq_2026.items()
    if normalize(tok) not in freq_2025_normalized
    and cnt >= 5
    and tok.isalpha()
    and len(tok) >= 4
}

neologisms_sorted = sorted(neologisms.items(), key=lambda x: -x[1])

with open('neologisms_final.json', 'w', encoding='utf-8') as f:
    json.dump(neologisms_sorted[:5000], f, ensure_ascii=False, indent=2)

print(f"Total real neologisms: {len(neologisms_sorted)}")
print("Top 20:")
for word, count in neologisms_sorted[:20]:
    print(f"  {word}: {count}")
