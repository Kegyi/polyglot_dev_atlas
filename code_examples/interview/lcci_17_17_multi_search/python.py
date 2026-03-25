from typing import List


class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.idx = -1

    def insert(self, word: str, i: int):
        node = self
        for c in word:
            j = ord(c) - ord('a')
            if node.children[j] is None:
                node.children[j] = Trie()
            node = node.children[j]
        node.idx = i


class Solution:
    def multiSearch(self, big: str, smalls: List[str]) -> List[List[int]]:
        trie = Trie()
        for i, s in enumerate(smalls):
            if s:
                trie.insert(s, i)

        ans = [[] for _ in smalls]
        for i in range(len(big)):
            node = trie
            for j in range(i, len(big)):
                k = ord(big[j]) - ord('a')
                if node.children[k] is None:
                    break
                node = node.children[k]
                if node.idx != -1:
                    ans[node.idx].append(i)
        return ans
