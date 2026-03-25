from typing import List
from collections import deque


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[str]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []
        queue = deque([[beginWord]])
        visited = {beginWord}
        while queue:
            path = queue.popleft()
            cur = path[-1]
            for i in range(len(cur)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    nxt = cur[:i] + c + cur[i+1:]
                    if nxt == endWord:
                        return path + [endWord]
                    if nxt in word_set and nxt not in visited:
                        visited.add(nxt)
                        queue.append(path + [nxt])
        return []
