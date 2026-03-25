#include <iostream>
#include <random>

int main() {
    std::mt19937 generator(42);
    std::uniform_int_distribution<int> dist(1, 10);

    std::cout << "draws: ";
    for (int i = 0; i < 3; ++i) {
        std::cout << dist(generator) << ' ';
    }
    std::cout << "\n";
    return 0;
}
