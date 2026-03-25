#include <iostream>
#include <vector>

void rotate(std::vector<std::vector<int>>& m) {
    const int n = static_cast<int>(m.size());
    for (int layer = 0; layer < n / 2; ++layer) {
        int first = layer;
        int last = n - 1 - layer;
        for (int i = first; i < last; ++i) {
            int offset = i - first;
            int top = m[first][i];
            m[first][i] = m[last - offset][first];
            m[last - offset][first] = m[last][last - offset];
            m[last][last - offset] = m[i][last];
            m[i][last] = top;
        }
    }
}

int main() {
    std::vector<std::vector<int>> m = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    rotate(m);

    for (const auto& row : m) {
        std::cout << row[0] << ' ' << row[1] << ' ' << row[2] << '\n';
    }
    return 0;
}
