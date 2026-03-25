#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

vector<double> cutSquares(const vector<int>& square1, const vector<int>& square2) {
    double x1 = square1[0], y1 = square1[1], s1 = square1[2];
    double x2 = square2[0], y2 = square2[1], s2 = square2[2];

    double cx1 = x1 + s1 / 2.0, cy1 = y1 + s1 / 2.0;
    double cx2 = x2 + s2 / 2.0, cy2 = y2 + s2 / 2.0;

    const double eps = 1e-9;
    if (fabs(cx1 - cx2) < eps) {
        double x = cx1;
        double yBottom = min(y1, y2);
        double yTop = max(y1 + s1, y2 + s2);
        return {x, yBottom, x, yTop};
    }

    double k = (cy2 - cy1) / (cx2 - cx1);
    double b = cy1 - k * cx1;

    double px1, py1, px2, py2;
    if (fabs(k) <= 1) {
        px1 = min(x1, x2);
        px2 = max(x1 + s1, x2 + s2);
        py1 = k * px1 + b;
        py2 = k * px2 + b;
    } else {
        py1 = min(y1, y2);
        py2 = max(y1 + s1, y2 + s2);
        px1 = (py1 - b) / k;
        px2 = (py2 - b) / k;
    }

    if (px1 > px2 || (fabs(px1 - px2) < eps && py1 > py2)) {
        swap(px1, px2);
        swap(py1, py2);
    }
    return {px1, py1, px2, py2};
}

int main() {
    vector<double> ans = cutSquares({-1, -1, 2}, {0, -1, 2});
    cout << "[" << ans[0] << ", " << ans[1] << ", " << ans[2] << ", " << ans[3] << "]" << endl;
    return 0;
}
