#include <iostream>
#include <vector>
#include <functional>
using namespace std;

vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
    int old = image[sr][sc];
    if (old == newColor) return image;
    int r = image.size(), c = image[0].size();
    function<void(int, int)> dfs = [&](int i, int j) {
        if (i < 0 || i >= r || j < 0 || j >= c || image[i][j] != old) return;
        image[i][j] = newColor;
        dfs(i + 1, j); dfs(i - 1, j); dfs(i, j + 1); dfs(i, j - 1);
    };
    dfs(sr, sc);
    return image;
}

int main() {
    vector<vector<int>> image = {{1,1,1},{1,1,0},{1,0,1}};
    auto result = floodFill(image, 1, 1, 2);
    for (auto& row : result) {
        for (int i = 0; i < (int)row.size(); i++) {
            cout << row[i] << (i + 1 < (int)row.size() ? " " : "\n");
        }
    }
    return 0;
}
