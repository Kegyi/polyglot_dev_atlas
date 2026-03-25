from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        word_set = set(words)

        def can_build(w: str) -> bool:
            if not w:
                return True
            for i in range(1, len(w) + 1):
                if w[:i] in word_set and can_build(w[i:]):
                    return True
            return False

        words.sort(key=lambda x: (-len(x), x))
        for w in words:
            word_set.discard(w)
            if can_build(w):
                return w
            word_set.add(w)
        return ""
