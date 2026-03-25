#include <iostream>
#include <string>
#include <vector>
using namespace std;

const int MOD = 1e9 + 7;

int countEval(string s, int result) {
    int n = s.size();
    // dp[i][j][v] = ways to evaluate s[i..j] to v (0 or 1)
    // s has digits at even indices, operators at odd indices
    int len = (n + 1) / 2; // number of operands
    vector<vector<array<long long,2>>> dp(n, vector<array<long long,2>>(n, {0,0}));
    for (int i = 0; i < n; i += 2) {
        dp[i][i][s[i] - '0'] = 1;
    }
    for (int size = 3; size <= n; size += 2) {
        for (int i = 0; i <= n - size; i += 2) {
            int j = i + size - 1;
            for (int k = i + 1; k < j; k += 2) {
                char op = s[k];
                long long lf = dp[i][k-1][0], lt = dp[i][k-1][1];
                long long rf = dp[k+1][j][0], rt = dp[k+1][j][1];
                if (op == '&') {
                    dp[i][j][1] = (dp[i][j][1] + lt * rt) % MOD;
                    dp[i][j][0] = (dp[i][j][0] + lf*rf + lf*rt + lt*rf) % MOD;
                } else if (op == '|') {
                    dp[i][j][1] = (dp[i][j][1] + lt*rt + lf*rt + lt*rf) % MOD;
                    dp[i][j][0] = (dp[i][j][0] + lf * rf) % MOD;
                } else { // '^'
                    dp[i][j][1] = (dp[i][j][1] + lf*rt + lt*rf) % MOD;
                    dp[i][j][0] = (dp[i][j][0] + lf*rf + lt*rt) % MOD;
                }
            }
        }
    }
    return (int)dp[0][n-1][result];
}

int main() {
    cout << countEval("1^0|0|1", 0) << endl; // 2
    cout << countEval("0&0&0&1^1|0", 1) << endl; // 10
    return 0;
}
