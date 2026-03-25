from collections import Counter
from typing import List


class WordsFrequency:
    def __init__(self, book: List[str]):
        self.counter = Counter(book)

    def get(self, word: str) -> int:
        return self.counter.get(word, 0)


def main() -> None:
    wf = WordsFrequency(["i", "have", "an", "apple", "he", "have", "a", "pen"])
    print(wf.get("have"))
    print(wf.get("you"))


if __name__ == "__main__":
    main()
