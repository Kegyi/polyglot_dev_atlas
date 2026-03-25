#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int getKthMagicNumber(int k) {
        vector<long long> dp(k + 1);
        dp[1] = 1;
        int i3 = 1, i5 = 1, i7 = 1;
        for (int i = 2; i <= k; i++) {
            long long a = dp[i3] * 3;
            long long b = dp[i5] * 5;
            long long c = dp[i7] * 7;
            dp[i] = min(a, min(b, c));
            if (dp[i] == a) i3++;
            if (dp[i] == b) i5++;
            if (dp[i] == c) i7++;
        }
        return (int)dp[k];
    }
};

int main() {
    Solution sol;
    cout << sol.getKthMagicNumber(5) << endl; // 9
    cout << sol.getKthMagicNumber(1) << endl; // 1
    return 0;
}
