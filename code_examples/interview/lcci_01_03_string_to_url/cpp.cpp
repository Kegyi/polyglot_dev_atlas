#include <iostream>
#include <string>

std::string urlify(const std::string& s, int trueLength) {
    std::string out;
    out.reserve(static_cast<size_t>(trueLength) * 3);

    for (int i = 0; i < trueLength; ++i) {
        if (s[static_cast<size_t>(i)] == ' ') {
            out += "%20";
        } else {
            out.push_back(s[static_cast<size_t>(i)]);
        }
    }

    return out;
}

int main() {
    const std::string input = "Mr John Smith    ";
    std::cout << urlify(input, 13) << '\n';
    return 0;
}
