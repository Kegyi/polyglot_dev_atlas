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
            if used[i]:
                continue
            # Skip duplicate: if chars[i] == chars[i-1] and chars[i-1] was not used in this branch
            if i > 0 and chars[i] == chars[i - 1] and not used[i - 1]:
                continue
            used[i] = True
            path.append(c)
            backtrack(path)
            path.pop()
            used[i] = False

    backtrack([])
    return result

def main():
    for p in permutation("qqe"):
        print(p)

if __name__ == "__main__":
    main()
