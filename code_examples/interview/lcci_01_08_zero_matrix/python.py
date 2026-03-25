def set_zeroes(matrix: list[list[int]]) -> None:
    rows = set()
    cols = set()

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 0:
                rows.add(r)
                cols.add(c)

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if r in rows or c in cols:
                matrix[r][c] = 0


def main() -> None:
    matrix = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 8, 9],
    ]

    set_zeroes(matrix)
    for row in matrix:
        print(*row)


if __name__ == "__main__":
    main()
