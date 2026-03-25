#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>
using namespace std;

string key(int r, int c) {
    return to_string(r) + "#" + to_string(c);
}

vector<string> printKMoves(int k) {
    int r = 0, c = 0, dir = 0;
    vector<int> dr = {0, 1, 0, -1};
    vector<int> dc = {1, 0, -1, 0};
    string dirs = "RDLU";

    unordered_set<string> black;
    int minR = 0, maxR = 0, minC = 0, maxC = 0;

    for (int step = 0; step < k; ++step) {
        string cur = key(r, c);
        if (black.count(cur)) {
            black.erase(cur);
            dir = (dir + 3) % 4;
        } else {
            black.insert(cur);
            dir = (dir + 1) % 4;
        }
        r += dr[dir];
        c += dc[dir];
        minR = min(minR, r);
        maxR = max(maxR, r);
        minC = min(minC, c);
        maxC = max(maxC, c);
    }

    for (const string& p : black) {
        size_t pos = p.find('#');
        int br = stoi(p.substr(0, pos));
        int bc = stoi(p.substr(pos + 1));
        minR = min(minR, br);
        maxR = max(maxR, br);
        minC = min(minC, bc);
        maxC = max(maxC, bc);
    }

    vector<string> board;
    for (int i = minR; i <= maxR; ++i) {
        string row;
        for (int j = minC; j <= maxC; ++j) {
            if (i == r && j == c) row.push_back(dirs[dir]);
            else if (black.count(key(i, j))) row.push_back('X');
            else row.push_back('_');
        }
        board.push_back(row);
    }
    return board;
}

int main() {
    vector<string> board = printKMoves(2);
    cout << "[";
    for (int i = 0; i < static_cast<int>(board.size()); ++i) {
        if (i) cout << ", ";
        cout << board[i];
    }
    cout << "]" << endl;
    return 0;
}
