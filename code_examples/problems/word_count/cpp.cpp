#include <iostream>
#include <fstream>
#include <string>
#include <unordered_map>
#include <vector>
#include <algorithm>
#include <cctype>

int main(int argc, char** argv) {
    std::string path = (argc > 1) ? argv[1] : "data.txt";
    std::ifstream in(path);
    if (!in) { std::cerr << "Cannot open " << path << std::endl; return 1; }
    std::unordered_map<std::string,int> counts;
    std::string token;
    while (in >> token) {
        std::string w;
        for (char ch : token) {
            if (std::isalpha(static_cast<unsigned char>(ch))) w.push_back(std::tolower(static_cast<unsigned char>(ch)));
        }
        if (!w.empty()) ++counts[w];
    }
    std::vector<std::pair<std::string,int>> vec(counts.begin(), counts.end());
    std::sort(vec.begin(), vec.end(), [](const auto& a, const auto& b){ return a.second > b.second; });
    for (const auto& p : vec) std::cout << p.first << ": " << p.second << std::endl;
    return 0;
}
