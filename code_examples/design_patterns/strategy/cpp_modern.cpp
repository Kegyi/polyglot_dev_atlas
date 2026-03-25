// Modern C++ Strategy using policy-based templates (compile-time) and std::function (runtime)
// No virtual dispatch, no heap allocation for small strategies.
#include <iostream>
#include <functional>

// --- Approach 1: Policy-based design (compile-time strategy selection) ---
// Each strategy is a plain callable type; zero overhead at runtime.

struct Add      { int operator()(int a, int b) const { return a + b; } };
struct Subtract { int operator()(int a, int b) const { return a - b; } };
struct Multiply { int operator()(int a, int b) const { return a * b; } };

template<typename Policy>
class Calculator {
public:
    int execute(int a, int b) const { return Policy{}(a, b); }
};

// --- Approach 2: std::function (runtime strategy selection) ---
// Lambdas and free functions slot in directly; no strategy base class needed.

class DynamicCalculator {
public:
    using Strategy = std::function<int(int, int)>;

    explicit DynamicCalculator(Strategy strategy) : strategy_(std::move(strategy)) {}

    int execute(int a, int b) const { return strategy_(a, b); }

private:
    Strategy strategy_;
};

int main() {
    // Compile-time selection – different types, resolved at compile time
    Calculator<Add>      adder;
    Calculator<Subtract> subtractor;
    Calculator<Multiply> multiplier;

    std::cout << "Add: "      << adder.execute(5, 3)      << '\n';
    std::cout << "Subtract: " << subtractor.execute(5, 3) << '\n';
    std::cout << "Multiply: " << multiplier.execute(5, 3) << '\n';

    // Runtime selection via lambda – swap strategy without recompiling
    DynamicCalculator calc([](int a, int b) { return a + b; });
    std::cout << "Dynamic add: " << calc.execute(5, 3) << '\n';

    calc = DynamicCalculator([](int a, int b) { return a * b; });
    std::cout << "Dynamic mul: " << calc.execute(5, 3) << '\n';
}
