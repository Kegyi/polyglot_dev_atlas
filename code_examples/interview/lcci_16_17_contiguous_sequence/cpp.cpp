#include <iostream>
#include <vector>
using namespace std;

int maxSubArray(const vector<int>& nums) {
    int best = nums[0];
    int cur = nums[0];
    for (int i = 1; i < static_cast<int>(nums.size()); ++i) {
        cur = max(nums[i], cur + nums[i]);
        best = max(best, cur);
    }
    return best;
}

int main() {
    cout << maxSubArray({-2, 1, -3, 4, -1, 2, 1, -5, 4}) << endl;
    return 0;
}
