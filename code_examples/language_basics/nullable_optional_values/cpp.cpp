#include <iostream>
#include <optional>
#include <string>

std::optional<int> parse_age(const std::string& text) {
    if (text.empty()) {
        return std::nullopt;
    }
    return std::stoi(text);
}

int main() {
    auto age = parse_age("29");
    auto missing = parse_age("");

    std::cout << "age present: " << age.has_value() << "\n";
    std::cout << "missing default: " << missing.value_or(0) << "\n";
    return 0;
}
