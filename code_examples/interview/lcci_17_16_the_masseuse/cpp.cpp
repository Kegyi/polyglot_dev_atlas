#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int massage(vector<int>& nums) {
        int f = 0, g = 0;
        for (int x : nums) {
            int nf = g + x;
            int ng = max(f, g);
            f = nf;
            g = ng;
        }
        return max(f, g);
    }
};
