#include <functional>
#include <iostream>
#include <numeric>
#include <string>

int main() {
    std::string text = "hello-world";

    std::size_t hash_value = std::hash<std::string>{}(text);
    int checksum = std::accumulate(text.begin(), text.end(), 0);

    std::cout << "text: " << text << "\n";
    std::cout << "hash: " << hash_value << "\n";
    std::cout << "checksum: " << checksum << "\n";
    return 0;
}
