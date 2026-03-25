#include <array>
#include <iostream>
#include <string>

bool checkPermutation(const std::string& a, const std::string& b) {
    if (a.size() != b.size()) {
        return false;
    }

    std::array<int, 256> freq{};
    for (unsigned char ch : a) {
        ++freq[ch];
    }
    for (unsigned char ch : b) {
        --freq[ch];
        if (freq[ch] < 0) {
            return false;
        }
    }
    return true;
}

int main() {
    std::cout << "abcde vs edcba -> " << std::boolalpha << checkPermutation("abcde", "edcba") << '\n';
    std::cout << "abc vs abz -> " << std::boolalpha << checkPermutation("abc", "abz") << '\n';
    return 0;
}
