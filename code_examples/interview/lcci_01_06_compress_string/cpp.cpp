#include <iostream>
#include <string>

std::string compressString(const std::string& s) {
    if (s.empty()) {
        return s;
    }

    std::string out;
    out.reserve(s.size());

    int run = 1;
    for (std::size_t i = 1; i <= s.size(); ++i) {
        if (i < s.size() && s[i] == s[i - 1]) {
            ++run;
            continue;
        }

        out.push_back(s[i - 1]);
        out += std::to_string(run);
        run = 1;
    }

    return out.size() < s.size() ? out : s;
}

int main() {
    std::cout << "aabcccccaaa -> " << compressString("aabcccccaaa") << '\n';
    std::cout << "abbccd -> " << compressString("abbccd") << '\n';
    return 0;
}
