#include <iostream>

// Count the number of bits you must flip to convert integer A to integer B.
int convertInteger(int A, int B) {
    unsigned int x = (unsigned int)(A ^ B);
    int count = 0;
    while (x) { count += x & 1; x >>= 1; }
    return count;
}

int main() {
    std::cout << convertInteger(29, 15) << '\n';  // 29=11101, 15=01111 -> 2 bits differ
    std::cout << convertInteger(1, 5)  << '\n';  //  1=001, 5=101   -> 1 bit differs
}
