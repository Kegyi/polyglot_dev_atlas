#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<vector<int>> subsets(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    int n = nums.size();
    vector<vector<int>> result;
    for (int mask = 0; mask < (1 << n); mask++) {
        vector<int> subset;
        for (int i = 0; i < n; i++) {
            if (mask & (1 << i)) subset.push_back(nums[i]);
        }
        result.push_back(subset);
    }
    return result;
}

int main() {
    vector<int> nums = {1, 2, 3};
    auto result = subsets(nums);
    for (auto& s : result) {
        cout << "[";
        for (int i = 0; i < (int)s.size(); i++) {
            cout << s[i];
            if (i + 1 < (int)s.size()) cout << ",";
        }
        cout << "]" << endl;
    }
    return 0;
}
