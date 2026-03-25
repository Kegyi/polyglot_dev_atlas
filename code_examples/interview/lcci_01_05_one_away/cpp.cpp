#include <cstdlib>
#include <iostream>
#include <string>

bool oneAway(const std::string& a, const std::string& b) {
    if (std::abs(static_cast<int>(a.size()) - static_cast<int>(b.size())) > 1) {
        return false;
    }

    const std::string& s1 = a.size() <= b.size() ? a : b;
    const std::string& s2 = a.size() <= b.size() ? b : a;

    std::size_t i = 0;
    std::size_t j = 0;
    bool foundDiff = false;

    while (i < s1.size() && j < s2.size()) {
        if (s1[i] == s2[j]) {
            ++i;
            ++j;
            continue;
        }

        if (foundDiff) {
            return false;
        }
        foundDiff = true;

        if (s1.size() == s2.size()) {
            ++i;
        }
        ++j;
    }

    return true;
}

int main() {
    std::cout << "pale vs ple -> " << std::boolalpha << oneAway("pale", "ple") << '\n';
    std::cout << "pales vs pale -> " << std::boolalpha << oneAway("pales", "pale") << '\n';
    std::cout << "pale vs bake -> " << std::boolalpha << oneAway("pale", "bake") << '\n';
    return 0;
}
