from typing import List

def permutation(S: str) -> List[str]:
    result = []
    chars = sorted(S)
    used = [False] * len(chars)

    def backtrack(path):
        if len(path) == len(chars):
            result.append("".join(path))
            return
        for i, c in enumerate(chars):
            if not used[i]:
                used[i] = True
                path.append(c)
                backtrack(path)
                path.pop()
                used[i] = False

    backtrack([])
    return result

def main():
    for p in permutation("qwe"):
        print(p)

if __name__ == "__main__":
    main()
