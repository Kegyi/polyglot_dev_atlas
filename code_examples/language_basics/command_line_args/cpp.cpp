#include <iostream>
#include <string>

int main(int argc, char** argv) {
    std::string name = argc > 1 ? argv[1] : "world";
    bool excited = argc > 2 && std::string(argv[2]) == "--excited";

    std::cout << "Hello, " << name;
    if (excited) {
        std::cout << "!";
    }
    std::cout << "\n";
    return 0;
}
