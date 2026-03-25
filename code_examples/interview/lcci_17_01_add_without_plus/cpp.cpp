#include <iostream>
using namespace std;

class Solution {
public:
    int add(int a, int b) {
        while (b != 0) {
            unsigned int carry = (unsigned int)(a & b) << 1;
            a = a ^ b;
            b = (int)carry;
        }
        return a;
    }
};

int main() {
    Solution sol;
    cout << sol.add(1, 2) << endl;    // 3
    cout << sol.add(3, -2) << endl;   // 1
    cout << sol.add(-1, -2) << endl;  // -3
    return 0;
}
