#include <iostream>
#include <string>
#include <vector>
using namespace std;

string tictactoe(const vector<string>& board) {
    int n = board.size();
    auto winner = [&](char c) {
        for (int i = 0; i < n; ++i) {
            bool row = true, col = true;
            for (int j = 0; j < n; ++j) {
                row = row && board[i][j] == c;
                col = col && board[j][i] == c;
            }
            if (row || col) return true;
        }
        bool diag1 = true, diag2 = true;
        for (int i = 0; i < n; ++i) {
            diag1 = diag1 && board[i][i] == c;
            diag2 = diag2 && board[i][n - 1 - i] == c;
        }
        return diag1 || diag2;
    };

    if (winner('X')) return "X";
    if (winner('O')) return "O";
    for (const string& row : board) {
        for (char ch : row) {
            if (ch == ' ') return "Pending";
        }
    }
    return "Draw";
}

int main() {
    cout << tictactoe({"O X", " XO", "X O"}) << endl;
    cout << tictactoe({"OOX", "XXO", "OXO"}) << endl;
    return 0;
}
