#include <array>
#include <iostream>
#include <queue>
#include <utility>
#include <vector>

int shortestPathSteps(const std::vector<std::vector<int>>& grid) {
    const int rows = static_cast<int>(grid.size());
    const int cols = static_cast<int>(grid[0].size());
    if (grid[0][0] == 1 || grid[rows - 1][cols - 1] == 1) {
        return -1;
    }

    std::vector<std::vector<int>> dist(rows, std::vector<int>(cols, -1));
    std::queue<std::pair<int, int>> q;
    q.push({0, 0});
    dist[0][0] = 0;

    const std::array<std::pair<int, int>, 4> dirs = {{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}};

    while (!q.empty()) {
        auto [r, c] = q.front();
        q.pop();

        if (r == rows - 1 && c == cols - 1) {
            return dist[r][c];
        }

        for (auto [dr, dc] : dirs) {
            int nr = r + dr;
            int nc = c + dc;
            if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) {
                continue;
            }
            if (grid[nr][nc] == 1 || dist[nr][nc] != -1) {
                continue;
            }
            dist[nr][nc] = dist[r][c] + 1;
            q.push({nr, nc});
        }
    }

    return -1;
}

int main() {
    const std::vector<std::vector<int>> grid = {
        {0, 0, 1, 0, 0},
        {1, 0, 1, 0, 1},
        {0, 0, 0, 0, 0},
        {0, 1, 1, 1, 0},
        {0, 0, 0, 1, 0}
    };

    std::cout << "shortest steps: " << shortestPathSteps(grid) << '\n';
    return 0;
}
