#include <cstdlib>
#include <iostream>
#include <string>

int main() {
    const char* mode_raw = std::getenv("APP_MODE");
    const char* port_raw = std::getenv("APP_PORT");

    std::string mode = mode_raw ? mode_raw : "development";
    std::string port = port_raw ? port_raw : "8080";

    std::cout << "mode: " << mode << "\n";
    std::cout << "port: " << port << "\n";
    std::cout << "has APP_MODE: " << (mode_raw != nullptr) << "\n";
    return 0;
}
