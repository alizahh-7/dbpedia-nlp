import json

with open('freq_2026.json', 'r', encoding='utf-8') as f:
    freq_2026 = json.load(f)

with open('freq_2025.json', 'r', encoding='utf-8') as f:
    freq_2025 = json.load(f)

# Proper neologisms - minimum 5 occurrences, purely alphabetic
neologisms = {
    tok: cnt for tok, cnt in freq_2026.items() 
    if tok not in freq_2025 
    and cnt >= 5
    and tok.isalpha()
    and len(tok) >= 4
}

neologisms_sorted = sorted(neologisms.items(), key=lambda x: -x[1])

with open('neologisms_clean.json', 'w', encoding='utf-8') as f:
    json.dump(neologisms_sorted[:5000], f, ensure_ascii=False, indent=2)

print(f"Total clean neologisms: {len(neologisms_sorted)}")
print("Top 20:")
for word, count in neologisms_sorted[:20]:
    print(f"  {word}: {count}")
