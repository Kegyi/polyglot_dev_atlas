#include <iostream>
#include <vector>

// Return the next smaller and next larger numbers with the same popcount.
// Returns {next smaller, next larger}.
std::vector<int> findClosedNumbers(int num) {
    int bigger = num, smaller = num;

    // Next larger: find rightmost 01 pattern and flip
    for (int i = 1; i < 32; i++) {
        if ((bigger & (1 << (i - 1))) && !(bigger & (1 << i))) {
            bigger |= (1 << i);
            bigger &= ~(1 << (i - 1));
            break;
        }
    }

    // Next smaller: find rightmost 10 pattern and flip
    for (int i = 1; i < 32; i++) {
        if (!(smaller & (1 << (i - 1))) && (smaller & (1 << i))) {
            smaller &= ~(1 << i);
            smaller |= (1 << (i - 1));
            break;
        }
    }

    return {bigger, smaller};
}

int main() {
    auto res = findClosedNumbers(2);  // 010 -> bigger=100(4), smaller=001(1)
    std::cout << res[0] << '\n' << res[1] << '\n';
}
