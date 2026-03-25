#include <iostream>
using namespace std;

int waysToStep(int n) {
    const long long MOD = 1e9 + 7;
    if (n == 1) return 1;
    if (n == 2) return 2;
    if (n == 3) return 4;
    long long a = 1, b = 2, c = 4;
    for (int i = 3; i < n; i++) {
        long long d = ((a + b) % MOD + c) % MOD;
        a = b; b = c; c = d;
    }
    return (int)c;
}

int main() {
    cout << waysToStep(3) << endl; // 4
    cout << waysToStep(5) << endl; // 13
    return 0;
}
