import json

with open('freq_2026.json', 'r', encoding='utf-8') as f:
    freq_2026 = json.load(f)

with open('freq_2025.json', 'r', encoding='utf-8') as f:
    freq_2025 = json.load(f)

print(f"2026 vocab size (saved): {len(freq_2026)}")
print(f"2025 vocab size (saved): {len(freq_2025)}")
print(f"2026 total tokens: {sum(freq_2026.values()):,}")
print(f"2025 total tokens: {sum(freq_2025.values()):,}")
print(f"Min frequency in 2026: {min(freq_2026.values())}")
print(f"Min frequency in 2025: {min(freq_2025.values())}")
