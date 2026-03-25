#include <fstream>
#include <iostream>
#include <string>
#include <vector>

int main() {
    const std::string path = "file_io_demo.txt";

    {
        std::ofstream out(path);
        out << "apple\nbanana\ncarrot\n";
    }

    std::ifstream in(path);
    std::vector<std::string> lines;
    for (std::string line; std::getline(in, line);) {
        lines.push_back(line);
    }

    std::cout << "read lines: ";
    for (const auto& line : lines) {
        std::cout << line << ' ';
    }
    std::cout << "\n";
    return 0;
}
