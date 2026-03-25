#!/usr/bin/env python3
from collections import Counter
import re
import sys

def word_count(path='data.txt'):
    with open(path, 'r', encoding='utf-8') as fh:
        text = fh.read().lower()
    words = re.findall(r"\b\w+\b", text)
    return Counter(words)

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else 'data.txt'
    cnt = word_count(path)
    for w, c in cnt.most_common():
        print(f"{w}: {c}")

if __name__ == '__main__':
    main()
