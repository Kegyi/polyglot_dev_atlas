#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int pileBox(vector<vector<int>>& box) {
    // Sort by width descending, then depth descending
    sort(box.begin(), box.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[0] != b[0] ? a[0] > b[0] : a[1] > b[1];
    });
    int n = box.size();
    // dp[i] = max height with box[i] on top
    vector<int> dp(n);
    for (int i = 0; i < n; i++) dp[i] = box[i][2];
    int ans = *max_element(dp.begin(), dp.end());
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (box[j][0] > box[i][0] && box[j][1] > box[i][1] && box[j][2] > box[i][2]) {
                dp[i] = max(dp[i], dp[j] + box[i][2]);
            }
        }
        ans = max(ans, dp[i]);
    }
    return ans;
}

int main() {
    vector<vector<int>> box = {{2,2,2},{3,3,3},{4,4,4}};
    cout << pileBox(box) << endl; // 9
    return 0;
}
