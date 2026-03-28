import bz2, re, json
from collections import Counter
from tqdm import tqdm

def clean_text(text):
    text = re.sub(r'\[\[([^|\]]*\|)?([^\]]*)\]\]', r'\2', text)
    text = re.sub(r'\{\{[^}]*\}\}', '', text)
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'={2,}[^=]+=+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def tokenize(text):
    return re.findall(r'\b[a-záéíóúüñ]{3,}\b', text.lower())

def process_dump(filepath):
    freq = Counter()
    articles = 0
    with bz2.open(filepath, 'rt', encoding='utf-8') as f:
        buffer = []
        in_text = False
        for line in tqdm(f, desc=filepath):
            if '<text' in line:
                in_text = True
            if in_text:
                buffer.append(line)
            if '</text>' in line:
                in_text = False
                raw = ''.join(buffer)
                raw = re.sub(r'<.*?>', '', raw, flags=re.DOTALL)
                cleaned = clean_text(raw)
                tokens = tokenize(cleaned)
                freq.update(tokens)
                articles += 1
                buffer = []
    print(f"Articles: {articles}, Unique tokens: {len(freq)}")
    return freq

freq_2026 = process_dump('eswiki-20260301-pages-articles.xml.bz2')

with open('freq_2026.json', 'w', encoding='utf-8') as f:
    json.dump(dict(freq_2026.most_common(100000)), f, ensure_ascii=False, indent=2)

print("Done! freq_2026.json saved!")
