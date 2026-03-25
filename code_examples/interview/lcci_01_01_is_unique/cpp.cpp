#include <array>
#include <iostream>
#include <string>

bool isUnique(const std::string& s) {
    std::array<bool, 256> seen{};
    for (unsigned char ch : s) {
        if (seen[ch]) {
            return false;
        }
        seen[ch] = true;
    }
    return true;
}

int main() {
    std::cout << "leetcode -> " << std::boolalpha << isUnique("leetcode") << '\n';
    std::cout << "abc -> " << std::boolalpha << isUnique("abc") << '\n';
    return 0;
}
