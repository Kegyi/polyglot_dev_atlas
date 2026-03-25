#include <iostream>
#include <vector>
using namespace std;

bool collinear(const vector<int>& a, const vector<int>& b, const vector<int>& c) {
    long long x1 = b[0] - a[0], y1 = b[1] - a[1];
    long long x2 = c[0] - a[0], y2 = c[1] - a[1];
    return x1 * y2 == x2 * y1;
}

vector<int> bestLine(const vector<vector<int>>& points) {
    int n = points.size();
    int bestI = 0, bestJ = 1, bestCount = 2;
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            int count = 2;
            for (int k = j + 1; k < n; ++k) {
                if (collinear(points[i], points[j], points[k])) {
                    ++count;
                }
            }
            if (count > bestCount || (count == bestCount && (i < bestI || (i == bestI && j < bestJ)))) {
                bestCount = count;
                bestI = i;
                bestJ = j;
            }
        }
    }
    return {bestI, bestJ};
}

int main() {
    vector<int> ans = bestLine({{0, 0}, {1, 1}, {1, 0}, {2, 2}});
    cout << "[" << ans[0] << ", " << ans[1] << "]" << endl;
    return 0;
}
