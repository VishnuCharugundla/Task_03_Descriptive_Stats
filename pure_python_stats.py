import csv
from collections import Counter, defaultdict
import os

def summarize_column(data):
    summary = {
        'count': len(data),
        'unique': len(set(data)),
    }
    freq = Counter(data)
    summary['most_frequent'] = freq.most_common(1)[0] if freq else None
    return summary

def summarize_numeric(data):
    numeric = list(map(float, data))
    return {
        'count': len(numeric),
        'mean': sum(numeric) / len(numeric),
        'min': min(numeric),
        'max': max(numeric),
        'std': (sum((x - sum(numeric)/len(numeric))**2 for x in numeric) / len(numeric))**0.5
    }

def analyze(filepath):
    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = defaultdict(list)
        for row in reader:
            for key, value in row.items():
                if value != '':
                    data[key].append(value)

    print("\n--- Overall ---")
    for key, values in data.items():
        try:
            summary = summarize_numeric(values)
        except:
            summary = summarize_column(values)
        print(f"{key}: {summary}")

if __name__ == "__main__":
    analyze("data/2024_fb_ads_president_scored_anon.csv")
