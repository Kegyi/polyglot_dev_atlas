#include <iostream>
using namespace std;

class Solution {
public:
    int numberOf2sInRange(int n) {
        int count = 0;
        for (long long m = 1; m <= n; m *= 10) {
            long long a = n / m, b = n % m;
            if (a % 10 > 2) {
                count += (int)((a / 10 + 1) * m);
            } else if (a % 10 == 2) {
                count += (int)((a / 10) * m + b + 1);
            } else {
                count += (int)((a / 10) * m);
            }
        }
        return count;
    }
};

int main() {
    Solution sol;
    cout << sol.numberOf2sInRange(25) << endl;  // 9
    cout << sol.numberOf2sInRange(20) << endl;  // 2
    return 0;
}
