#include <iostream>
#include <vector>
#include <functional>
using namespace std;

vector<vector<int>> pathWithObstacles(vector<vector<int>>& obstacleGrid) {
    int r = obstacleGrid.size(), c = obstacleGrid[0].size();
    vector<vector<int>> path;
    vector<vector<bool>> visited(r, vector<bool>(c, false));

    function<bool(int, int)> dfs = [&](int i, int j) -> bool {
        if (i >= r || j >= c || obstacleGrid[i][j] == 1 || visited[i][j]) return false;
        visited[i][j] = true;
        path.push_back({i, j});
        if (i == r - 1 && j == c - 1) return true;
        if (dfs(i + 1, j) || dfs(i, j + 1)) return true;
        path.pop_back();
        return false;
    };

    dfs(0, 0);
    return path;
}

int main() {
    vector<vector<int>> grid = {{0,0,0},{0,1,0},{0,0,0}};
    auto path = pathWithObstacles(grid);
    cout << "[";
    for (int i = 0; i < (int)path.size(); i++) {
        cout << "[" << path[i][0] << "," << path[i][1] << "]";
        if (i + 1 < (int)path.size()) cout << ",";
    }
    cout << "]" << endl;
    return 0;
}
