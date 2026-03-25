#include <iostream>
#include <unordered_set>
#include <vector>

void setZeroes(std::vector<std::vector<int>>& matrix) {
    int rows = static_cast<int>(matrix.size());
    int cols = static_cast<int>(matrix[0].size());

    std::unordered_set<int> zeroRows;
    std::unordered_set<int> zeroCols;

    for (int r = 0; r < rows; ++r) {
        for (int c = 0; c < cols; ++c) {
            if (matrix[r][c] == 0) {
                zeroRows.insert(r);
                zeroCols.insert(c);
            }
        }
    }

    for (int r = 0; r < rows; ++r) {
        for (int c = 0; c < cols; ++c) {
            if (zeroRows.count(r) || zeroCols.count(c)) {
                matrix[r][c] = 0;
            }
        }
    }
}

int main() {
    std::vector<std::vector<int>> matrix = {
        {1, 2, 3},
        {4, 0, 6},
        {7, 8, 9}
    };

    setZeroes(matrix);

    for (const auto& row : matrix) {
        std::cout << row[0] << ' ' << row[1] << ' ' << row[2] << '\n';
    }
    return 0;
}
