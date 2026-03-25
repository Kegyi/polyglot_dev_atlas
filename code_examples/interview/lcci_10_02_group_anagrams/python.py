from collections import defaultdict
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    groups: dict[str, List[str]] = defaultdict(list)
    for word in strs:
        groups["".join(sorted(word))].append(word)
    result = [sorted(group) for group in groups.values()]
    result.sort(key=lambda group: group[0])
    return result


def main() -> None:
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


if __name__ == "__main__":
    main()
