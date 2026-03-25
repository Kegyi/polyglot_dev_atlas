#include <iostream>
#include <memory>
#include <string>

class Shape {
public:
    explicit Shape(std::string color) : color_(std::move(color)) {}
    virtual ~Shape() = default;
    virtual std::unique_ptr<Shape> clone() const = 0;
    virtual void describe() const = 0;

protected:
    std::string color_;
};

class Circle : public Shape {
public:
    Circle(std::string color, int radius) : Shape(std::move(color)), radius_(radius) {}

    std::unique_ptr<Shape> clone() const override {
        return std::make_unique<Circle>(*this);
    }

    void describe() const override {
        std::cout << color_ << " circle radius=" << radius_ << '\n';
    }

private:
    int radius_;
};

int main() {
    Circle templateCircle("blue", 12);
    auto copy = templateCircle.clone();
    templateCircle.describe();
    copy->describe();
}