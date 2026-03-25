#include <algorithm>
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

vector<vector<int>> pairSums(const vector<int>& nums, int target) {
    unordered_map<int, int> freq;
    vector<vector<int>> ans;
    for (int x : nums) {
        int y = target - x;
        if (freq[y] > 0) {
            --freq[y];
            ans.push_back({min(x, y), max(x, y)});
        } else {
            ++freq[x];
        }
    }
    return ans;
}

int main() {
    vector<vector<int>> ans = pairSums({5, 6, 5}, 11);
    cout << "[";
    for (int i = 0; i < static_cast<int>(ans.size()); ++i) {
        if (i) cout << ", ";
        cout << "[" << ans[i][0] << ", " << ans[i][1] << "]";
    }
    cout << "]" << endl;
    return 0;
}
