#include <iostream>
#include <vector>

int factorial(int n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

int sum_recursive(const std::vector<int>& values, size_t index = 0) {
    if (index >= values.size()) {
        return 0;
    }
    return values[index] + sum_recursive(values, index + 1);
}

int main() {
    std::vector<int> values{1, 2, 3, 4};
    std::cout << "factorial(5): " << factorial(5) << "\n";
    std::cout << "sum_recursive(values): " << sum_recursive(values) << "\n";
    return 0;
}
