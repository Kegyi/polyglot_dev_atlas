#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <functional>
using namespace std;

vector<vector<string>> solveNQueens(int n) {
    vector<vector<string>> result;
    set<int> usedCols, diag1, diag2;

    function<void(int, vector<string>&)> bt = [&](int row, vector<string>& board) {
        if (row == n) { result.push_back(board); return; }
        for (int col = 0; col < n; col++) {
            if (usedCols.count(col) || diag1.count(row - col) || diag2.count(row + col)) continue;
            board[row][col] = 'Q';
            usedCols.insert(col); diag1.insert(row - col); diag2.insert(row + col);
            bt(row + 1, board);
            board[row][col] = '.';
            usedCols.erase(col); diag1.erase(row - col); diag2.erase(row + col);
        }
    };

    vector<string> board(n, string(n, '.'));
    bt(0, board);
    return result;
}

int main() {
    auto result = solveNQueens(4);
    cout << result.size() << " solutions" << endl;
    for (auto& board : result) {
        for (auto& row : board) cout << row << endl;
        cout << endl;
    }
    return 0;
}
