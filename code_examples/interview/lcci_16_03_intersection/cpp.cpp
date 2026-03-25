#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

const double EPS = 1e-9;

bool lessPoint(const vector<double>& a, const vector<double>& b) {
    if (fabs(a[0] - b[0]) > EPS) return a[0] < b[0];
    return a[1] < b[1] - EPS;
}

double cross(const vector<double>& a, const vector<double>& b, const vector<double>& c) {
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]);
}

bool onSegment(const vector<double>& a, const vector<double>& b, const vector<double>& p) {
    return fabs(cross(a, b, p)) < EPS &&
           min(a[0], b[0]) - EPS <= p[0] && p[0] <= max(a[0], b[0]) + EPS &&
           min(a[1], b[1]) - EPS <= p[1] && p[1] <= max(a[1], b[1]) + EPS;
}

vector<double> intersection(vector<double> start1, vector<double> end1, vector<double> start2, vector<double> end2) {
    if (lessPoint(end1, start1)) swap(start1, end1);
    if (lessPoint(end2, start2)) swap(start2, end2);

    double d1 = cross(start1, end1, start2);
    double d2 = cross(start1, end1, end2);
    double d3 = cross(start2, end2, start1);
    double d4 = cross(start2, end2, end1);

    if (((d1 > EPS && d2 > EPS) || (d1 < -EPS && d2 < -EPS)) ||
        ((d3 > EPS && d4 > EPS) || (d3 < -EPS && d4 < -EPS))) {
        return {};
    }

    double a1 = end1[1] - start1[1];
    double b1 = start1[0] - end1[0];
    double c1 = a1 * start1[0] + b1 * start1[1];

    double a2 = end2[1] - start2[1];
    double b2 = start2[0] - end2[0];
    double c2 = a2 * start2[0] + b2 * start2[1];

    double det = a1 * b2 - a2 * b1;
    if (fabs(det) < EPS) {
        vector<vector<double>> candidates;
        if (onSegment(start1, end1, start2)) candidates.push_back(start2);
        if (onSegment(start1, end1, end2)) candidates.push_back(end2);
        if (onSegment(start2, end2, start1)) candidates.push_back(start1);
        if (onSegment(start2, end2, end1)) candidates.push_back(end1);
        if (candidates.empty()) return {};
        sort(candidates.begin(), candidates.end(), lessPoint);
        return candidates[0];
    }

    double x = (b2 * c1 - b1 * c2) / det;
    double y = (a1 * c2 - a2 * c1) / det;
    vector<double> p = {x, y};
    if (onSegment(start1, end1, p) && onSegment(start2, end2, p)) return p;
    return {};
}

int main() {
    vector<double> ans = intersection({0, 0}, {1, 0}, {1, 1}, {0, -1});
    if (ans.empty()) {
        cout << "[]" << endl;
    } else {
        cout << "[" << ans[0] << ", " << ans[1] << "]" << endl;
    }
    return 0;
}
