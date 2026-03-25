#include <iostream>
#include <optional>
#include <stdexcept>

int add(int a, int b) {
    return a + b;
}

std::optional<double> safe_div(double a, double b) {
    if (b == 0.0) {
        return std::nullopt;
    }
    return a / b;
}

int main() {
    std::cout << "add(2, 3): " << add(2, 3) << "\n";

    if (auto result = safe_div(10, 2)) {
        std::cout << "safe_div(10, 2): " << *result << "\n";
    }

    try {
        auto bad = safe_div(10, 0);
        if (!bad) {
            throw std::runtime_error("division by zero");
        }
    } catch (const std::exception& ex) {
        std::cerr << "error: " << ex.what() << "\n";
    }

    return 0;
}
