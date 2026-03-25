#include <iostream>
#include <string>

// Convert a decimal fraction (0 < n < 1) to its binary string representation.
// Return "ERROR" if the representation exceeds 32 characters.
std::string binaryToString(double n) {
    std::string result = "0.";
    while (n > 0) {
        if (result.size() > 32) return "ERROR";
        n *= 2;
        if (n >= 1) { result += '1'; n -= 1; }
        else result += '0';
    }
    return result;
}

int main() {
    std::cout << binaryToString(0.625) << '\n';
    std::cout << binaryToString(0.1) << '\n';
}
