#include <iostream>
#include <string>

int parse_port(const std::string& value) {
    return std::stoi(value);
}

int main() {
    try {
        int port = parse_port("not-a-number");
        std::cout << "port: " << port << "\n";
    } catch (const std::exception& ex) {
        std::cout << "parse failed: " << ex.what() << "\n";
        std::cout << "fallback port: 8080\n";
    }

    std::cout << "program continues\n";
    return 0;
}
