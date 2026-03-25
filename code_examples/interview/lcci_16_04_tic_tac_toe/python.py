from typing import List


def tictactoe(board: List[str]) -> str:
    n = len(board)

    def winner(c: str) -> bool:
        for i in range(n):
            if all(board[i][j] == c for j in range(n)):
                return True
            if all(board[j][i] == c for j in range(n)):
                return True
        if all(board[i][i] == c for i in range(n)):
            return True
        if all(board[i][n - 1 - i] == c for i in range(n)):
            return True
        return False

    if winner("X"):
        return "X"
    if winner("O"):
        return "O"
    if any(ch == " " for row in board for ch in row):
        return "Pending"
    return "Draw"


def main() -> None:
    print(tictactoe(["O X", " XO", "X O"]))
    print(tictactoe(["OOX", "XXO", "OXO"]))


if __name__ == "__main__":
    main()
