#include <algorithm>
#include <iostream>

// Find the longest sequence of 1s achievable by flipping one 0 bit.
int flipBit(int num) {
    if (~num == 0) return 32;  // all 1s already
    int cur = 0, prev = 0, best = 1;
    while (num > 0) {
        if (num & 1) { cur++; }
        else { prev = cur; cur = 0; }
        best = std::max(best, prev + 1 + cur);
        num >>= 1;
    }
    return best;
}

int main() {
    // 1775 = 11011101111, longest run after one flip = 8
    std::cout << flipBit(1775) << '\n';
    // 7 = 111, already 3 ones; flipping a 0 at bit 3 gives 4
    std::cout << flipBit(7) << '\n';
}
