from typing import List


def master_mind(solution: str, guess: str) -> List[int]:
    hits = 0
    cs = [0] * 26
    cg = [0] * 26
    for s, g in zip(solution, guess):
        if s == g:
            hits += 1
        else:
            cs[ord(s) - ord("A")] += 1
            cg[ord(g) - ord("A")] += 1
    pseudo = sum(min(cs[i], cg[i]) for i in range(26))
    return [hits, pseudo]


def main() -> None:
    print(master_mind("RGBY", "GGRR"))


if __name__ == "__main__":
    main()
