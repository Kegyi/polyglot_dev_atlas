#include <iostream>
#include <map>
#include <set>
#include <string>

int main() {
    std::map<std::string, int> counts;
    counts["apple"] = 2;
    counts["banana"] = 1;
    counts["apple"] += 3;

    std::set<std::string> tags{"fruit", "food"};
    tags.insert("fresh");

    std::cout << "apple count: " << counts["apple"] << "\n";

    std::cout << "all map entries: ";
    for (const auto& p : counts) {
        std::cout << "(" << p.first << "," << p.second << ") ";
    }
    std::cout << "\n";

    std::cout << "all set entries: ";
    for (const auto& t : tags) {
        std::cout << t << ' ';
    }
    std::cout << "\n";
    return 0;
}
