#include <iostream>

// Swap all odd and even bits of an integer.
// Odd bits (0-indexed): mask 0x55555555; even bits: mask 0xAAAAAAAA.
int exchangeBits(int num) {
    unsigned int unum = (unsigned int)num;
    return (int)(((unum & 0xAAAAAAAAu) >> 1) | ((unum & 0x55555555u) << 1));
}

int main() {
    // 2 = 010 -> after swap -> 001 = 1
    std::cout << exchangeBits(2) << '\n';
    // 3 = 011 -> 11 -> swap -> 11 = 3
    std::cout << exchangeBits(3) << '\n';
}
