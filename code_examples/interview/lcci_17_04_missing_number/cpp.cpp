#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int ans = 0;
        for (int i = 1; i <= (int)nums.size(); i++) {
            ans ^= i;
        }
        for (int x : nums) {
            ans ^= x;
        }
        return ans;
    }
};

int main() {
    Solution sol;
    vector<int> nums1 = {3, 0, 1};
    cout << sol.missingNumber(nums1) << endl;  // 2

    vector<int> nums2 = {9, 6, 4, 2, 3, 5, 7, 0, 1};
    cout << sol.missingNumber(nums2) << endl;  // 8
    return 0;
}
