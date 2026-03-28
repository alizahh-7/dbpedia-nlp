import json

print("Loading freq_2026...")
with open('freq_2026.json', 'r', encoding='utf-8') as f:
    freq_2026 = json.load(f)

print("Loading freq_2025...")
with open('freq_2025.json', 'r', encoding='utf-8') as f:
    freq_2025 = json.load(f)

# Neologisms = 2026 mein hain, 2025 mein nahi
neologisms = {tok: cnt for tok, cnt in freq_2026.items() if tok not in freq_2025}
neologisms_sorted = sorted(neologisms.items(), key=lambda x: -x[1])

with open('neologisms.json', 'w', encoding='utf-8') as f:
    json.dump(neologisms_sorted[:5000], f, ensure_ascii=False, indent=2)

print(f"Total neologisms: {len(neologisms_sorted)}")
print("Top 20 neologisms:")
for word, count in neologisms_sorted[:20]:
    print(f"  {word}: {count}")
