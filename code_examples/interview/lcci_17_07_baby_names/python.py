from typing import List
from collections import defaultdict


class Solution:
    def trulyMostPopular(self, names: List[str], synonyms: List[str]) -> List[str]:
        parent: dict = {}

        def find(x: str) -> str:
            if x not in parent:
                parent[x] = x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def unite(a: str, b: str) -> None:
            pa, pb = find(a), find(b)
            if pa != pb:
                if pa < pb:
                    parent[pb] = pa
                else:
                    parent[pa] = pb

        freq: dict = {}
        for s in names:
            paren = s.index('(')
            name = s[:paren]
            count = int(s[paren + 1:-1])
            freq[name] = count

        for syn in synonyms:
            s = syn[1:-1]
            comma = s.index(',')
            unite(s[:comma], s[comma + 1:])

        result: dict = defaultdict(int)
        for name, cnt in freq.items():
            result[find(name)] += cnt

        return sorted(f"{name}({cnt})" for name, cnt in result.items())


def main():
    sol = Solution()
    names = ["John(15)", "Jon(12)", "Chris(13)", "Kris(4)", "Christopher(19)"]
    synonyms = ["(Jon,John)", "(John,Johnny)", "(Chris,Kris)", "(Chris,Christopher)"]
    print(' '.join(sol.trulyMostPopular(names, synonyms)))  # Chris(36) John(27)


if __name__ == "__main__":
    main()
