from typing import List


def pond_sizes(land: List[List[int]]) -> List[int]:
    m, n = len(land), len(land[0])

    def dfs(r: int, c: int) -> int:
        if r < 0 or r >= m or c < 0 or c >= n or land[r][c] != 0:
            return 0
        land[r][c] = -1
        size = 1
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr != 0 or dc != 0:
                    size += dfs(r + dr, c + dc)
        return size

    ans = []
    for i in range(m):
        for j in range(n):
            if land[i][j] == 0:
                ans.append(dfs(i, j))
    ans.sort()
    return ans


def main() -> None:
    print(pond_sizes([[0, 2, 1, 0], [0, 1, 0, 1], [1, 1, 0, 1], [0, 1, 0, 1]]))


if __name__ == "__main__":
    main()
