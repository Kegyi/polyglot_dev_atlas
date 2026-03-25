#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int dfs(vector<vector<int>>& land, int r, int c) {
    int m = land.size(), n = land[0].size();
    if (r < 0 || r >= m || c < 0 || c >= n || land[r][c] != 0) return 0;
    land[r][c] = -1;
    int size = 1;
    for (int dr = -1; dr <= 1; ++dr) {
        for (int dc = -1; dc <= 1; ++dc) {
            if (dr != 0 || dc != 0) size += dfs(land, r + dr, c + dc);
        }
    }
    return size;
}

vector<int> pondSizes(vector<vector<int>> land) {
    vector<int> ans;
    int m = land.size(), n = land[0].size();
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (land[i][j] == 0) ans.push_back(dfs(land, i, j));
        }
    }
    sort(ans.begin(), ans.end());
    return ans;
}

int main() {
    vector<int> ans = pondSizes({{0, 2, 1, 0}, {0, 1, 0, 1}, {1, 1, 0, 1}, {0, 1, 0, 1}});
    cout << "[";
    for (int i = 0; i < static_cast<int>(ans.size()); ++i) {
        if (i) cout << ", ";
        cout << ans[i];
    }
    cout << "]" << endl;
    return 0;
}
