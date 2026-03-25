#include <iostream>
#include <string>

bool isStringRotation(const std::string& s1, const std::string& s2) {
    if (s1.size() != s2.size()) {
        return false;
    }
    return (s1 + s1).find(s2) != std::string::npos;
}

int main() {
    std::cout << "waterbottle vs erbottlewat -> "
              << std::boolalpha
              << isStringRotation("waterbottle", "erbottlewat")
              << '\n';
    std::cout << "aa vs aba -> "
              << std::boolalpha
              << isStringRotation("aa", "aba")
              << '\n';
    return 0;
}
