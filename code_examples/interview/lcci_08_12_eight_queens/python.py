from typing import List

def solveNQueens(n: int) -> List[List[str]]:
    result = []
    used_cols = set()
    diag1 = set()  # row - col
    diag2 = set()  # row + col

    def bt(row, board):
        if row == n:
            result.append(["".join(r) for r in board])
            return
        for col in range(n):
            if col in used_cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            board[row][col] = 'Q'
            used_cols.add(col); diag1.add(row - col); diag2.add(row + col)
            bt(row + 1, board)
            board[row][col] = '.'
            used_cols.remove(col); diag1.remove(row - col); diag2.remove(row + col)

    board = [['.' for _ in range(n)] for _ in range(n)]
    bt(0, board)
    return result

def main():
    result = solveNQueens(4)
    print(f"{len(result)} solutions")
    for board in result:
        for row in board:
            print(row)
        print()

if __name__ == "__main__":
    main()
