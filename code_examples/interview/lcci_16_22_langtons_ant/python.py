from typing import List, Set, Tuple


def print_k_moves(k: int) -> List[str]:
    r = c = 0
    dir_idx = 0
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    dirs = "RDLU"

    black: Set[Tuple[int, int]] = set()
    min_r = max_r = 0
    min_c = max_c = 0

    for _ in range(k):
        cur = (r, c)
        if cur in black:
            black.remove(cur)
            dir_idx = (dir_idx + 3) % 4
        else:
            black.add(cur)
            dir_idx = (dir_idx + 1) % 4
        r += dr[dir_idx]
        c += dc[dir_idx]
        min_r = min(min_r, r)
        max_r = max(max_r, r)
        min_c = min(min_c, c)
        max_c = max(max_c, c)

    for br, bc in black:
        min_r = min(min_r, br)
        max_r = max(max_r, br)
        min_c = min(min_c, bc)
        max_c = max(max_c, bc)

    board = []
    for i in range(min_r, max_r + 1):
        row = []
        for j in range(min_c, max_c + 1):
            if (i, j) == (r, c):
                row.append(dirs[dir_idx])
            elif (i, j) in black:
                row.append("X")
            else:
                row.append("_")
        board.append("".join(row))
    return board


def main() -> None:
    print(print_k_moves(2))


if __name__ == "__main__":
    main()
