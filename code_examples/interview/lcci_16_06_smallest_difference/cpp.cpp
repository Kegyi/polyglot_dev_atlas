#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

int smallestDifference(vector<int> a, vector<int> b) {
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    long long ans = LLONG_MAX;
    int i = 0, j = 0;
    while (i < static_cast<int>(a.size()) && j < static_cast<int>(b.size())) {
        long long x = a[i], y = b[j];
        ans = min(ans, llabs(x - y));
        if (x < y) ++i;
        else ++j;
    }
    return static_cast<int>(ans);
}

int main() {
    cout << smallestDifference({1, 3, 15, 11, 2}, {23, 127, 235, 19, 8}) << endl;
    return 0;
}
