// Modern C++ Visitor using std::variant + std::visit
// Eliminates double-dispatch ceremony; shapes are plain value types with no base class.
#include <iostream>
#include <variant>

struct Circle {
    void draw() const { std::cout << "Drawing circle\n"; }
};

struct Rectangle {
    void draw() const { std::cout << "Drawing rectangle\n"; }
};

using Shape = std::variant<Circle, Rectangle>;

// --- Named visitor struct ---
struct DrawVisitor {
    void operator()(const Circle& c)    const { c.draw(); }
    void operator()(const Rectangle& r) const { r.draw(); }
};

// --- Overload helper: compose lambdas into one callable (C++17) ---
template<class... Ts>
struct overload : Ts... { using Ts::operator()...; };

template<class... Ts>
overload(Ts...) -> overload<Ts...>;

int main() {
    Shape circle    = Circle{};
    Shape rectangle = Rectangle{};

    // Using a named visitor
    DrawVisitor draw;
    std::visit(draw, circle);
    std::visit(draw, rectangle);

    // Inline overload pattern – add a second "operation" without touching Shape types
    auto describe = overload{
        [](const Circle&)    { std::cout << "it's a circle\n"; },
        [](const Rectangle&) { std::cout << "it's a rectangle\n"; },
    };
    std::visit(describe, circle);
    std::visit(describe, rectangle);
}
