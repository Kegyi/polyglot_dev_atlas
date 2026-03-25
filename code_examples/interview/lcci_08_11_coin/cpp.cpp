#include <iostream>
#include <vector>
using namespace std;

int waysToChange(int n) {
    const int MOD = 1e9 + 7;
    int coins[] = {1, 5, 10, 25};
    vector<long long> dp(n + 1, 0);
    dp[0] = 1;
    for (int coin : coins) {
        for (int i = coin; i <= n; i++) {
            dp[i] = (dp[i] + dp[i - coin]) % MOD;
        }
    }
    return (int)dp[n];
}

int main() {
    cout << waysToChange(5)  << endl; // 2
    cout << waysToChange(10) << endl; // 4
    return 0;
}
