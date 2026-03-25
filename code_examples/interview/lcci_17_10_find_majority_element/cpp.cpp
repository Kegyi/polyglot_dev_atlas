#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int candidate = 0, count = 0;
        for (int x : nums) {
            if (count == 0) candidate = x;
            count += (x == candidate) ? 1 : -1;
        }
        count = 0;
        for (int x : nums) {
            if (x == candidate) count++;
        }
        return count > (int)nums.size() / 2 ? candidate : -1;
    }
};

int main() {
    Solution sol;
    vector<int> nums1 = {1, 2, 5, 9, 5, 9, 5, 5, 5};
    cout << sol.majorityElement(nums1) << endl; // 5

    vector<int> nums2 = {3, 2};
    cout << sol.majorityElement(nums2) << endl; // -1
    return 0;
}
