#include <bitset>
#include <iostream>

int countBits(int n) {
    int count = 0;
    while (n) { count += n & 1; n >>= 1; }
    return count;
}

int main() {
    int a = 0b1010, b = 0b1100;  // 10, 12
    std::cout << "a & b:  " << std::bitset<4>(a & b) << "\n";  // 1000
    std::cout << "a | b:  " << std::bitset<4>(a | b) << "\n";  // 1110
    std::cout << "a ^ b:  " << std::bitset<4>(a ^ b) << "\n";  // 0110

    int n = 0b0101;
    std::cout << "bit 1 set? " << ((n >> 1) & 1) << "\n";  // check -> 0
    n |= (1 << 2);                                          // set bit 2
    n &= ~(1 << 0);                                         // clear bit 0
    std::cout << "after set/clear: " << std::bitset<4>(n) << "\n";  // 0100

    std::cout << "count bits in 7: " << countBits(7) << "\n";  // 3
    return 0;
}
