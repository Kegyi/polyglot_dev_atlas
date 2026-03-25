#include <climits>
#include <iostream>
#include <vector>
using namespace std;

vector<int> subSort(const vector<int>& array) {
    int n = array.size();
    int left = -1, right = -1;

    int maxSeen = INT_MIN;
    for (int i = 0; i < n; ++i) {
        if (array[i] < maxSeen) right = i;
        else maxSeen = array[i];
    }

    int minSeen = INT_MAX;
    for (int i = n - 1; i >= 0; --i) {
        if (array[i] > minSeen) left = i;
        else minSeen = array[i];
    }

    if (left == -1) return {-1, -1};
    return {left, right};
}

int main() {
    vector<int> ans = subSort({1, 2, 4, 7, 10, 11, 7, 12, 7, 7, 16, 18, 19});
    cout << "[" << ans[0] << ", " << ans[1] << "]" << endl;
    return 0;
}
