#include <array>
#include <cctype>
#include <iostream>
#include <string>

bool canPermutePalindrome(const std::string& s) {
    std::array<int, 256> freq{};
    for (unsigned char ch : s) {
        if (std::isspace(ch)) {
            continue;
        }
        unsigned char lower = static_cast<unsigned char>(std::tolower(ch));
        ++freq[lower];
    }

    int odd = 0;
    for (int count : freq) {
        if ((count & 1) == 1) {
            ++odd;
            if (odd > 1) {
                return false;
            }
        }
    }
    return true;
}

int main() {
    std::cout << "tact coa -> " << std::boolalpha << canPermutePalindrome("tact coa") << '\n';
    std::cout << "daily -> " << std::boolalpha << canPermutePalindrome("daily") << '\n';
    return 0;
}
