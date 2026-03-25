#include <iostream>
#include <sstream>
#include <string>
#include <vector>

int main() {
    std::string first = "hello";
    std::string second = "world";
    std::string joined = first + " " + second;

    std::string part = joined.substr(0, 5);
    std::string replaced = joined;
    replaced.replace(0, 5, "hi");

    std::vector<std::string> words;
    std::istringstream iss(joined);
    for (std::string token; iss >> token;) {
        words.push_back(token);
    }

    std::cout << "joined: " << joined << "\n";
    std::cout << "part: " << part << "\n";
    std::cout << "replaced: " << replaced << "\n";
    std::cout << "tokens: ";
    for (const auto& w : words) {
        std::cout << w << ' ';
    }
    std::cout << "\n";
    return 0;
}
