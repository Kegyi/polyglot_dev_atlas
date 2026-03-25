#include <iostream>
#include <vector>
using namespace std;

bool searchMatrix(const vector<vector<int>>& matrix, int target) {
    if (matrix.empty() || matrix[0].empty()) {
        return false;
    }
    int row = 0;
    int col = static_cast<int>(matrix[0].size()) - 1;
    while (row < static_cast<int>(matrix.size()) && col >= 0) {
        if (matrix[row][col] == target) {
            return true;
        }
        if (matrix[row][col] > target) {
            --col;
        } else {
            ++row;
        }
    }
    return false;
}

int main() {
    vector<vector<int>> matrix = {
        {1, 4, 7, 11, 15},
        {2, 5, 8, 12, 19},
        {3, 6, 9, 16, 22},
        {10, 13, 14, 17, 24},
        {18, 21, 23, 26, 30}
    };
    cout << boolalpha << searchMatrix(matrix, 5) << endl;
    cout << boolalpha << searchMatrix(matrix, 20) << endl;
    return 0;
}
