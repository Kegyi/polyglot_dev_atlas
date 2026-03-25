#include <vector>
using namespace std;

class Solution {
public:
    vector<int> missingTwo(vector<int>& nums) {
        int n = nums.size() + 2;
        int xorVal = 0;
        for (int v : nums) xorVal ^= v;
        for (int i = 1; i <= n; ++i) xorVal ^= i;
        int diff = xorVal & (-xorVal);
        int a = 0;
        for (int v : nums) if (v & diff) a ^= v;
        for (int i = 1; i <= n; ++i) if (i & diff) a ^= i;
        int b = xorVal ^ a;
        return {a, b};
    }
};
