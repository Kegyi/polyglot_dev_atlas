#include <iostream>

// Insert bits of M into N from bit i to bit j (inclusive).
int insert(int N, int M, int i, int j) {
    int mask = ~(((1 << (j - i + 1)) - 1) << i);
    return (N & mask) | (M << i);
}

int main() {
    // N = 10000000000, M = 10011, i = 2, j = 6  -> 10001001100
    std::cout << insert(1024, 19, 2, 6) << '\n';
    // N = 0, M = 10011, i = 0, j = 4            -> 10011
    std::cout << insert(0, 19, 0, 4) << '\n';
}
