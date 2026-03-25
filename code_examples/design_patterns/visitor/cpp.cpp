#include <iostream>
#include <memory>

class Visitor;

class Element {
public:
    virtual ~Element() = default;
    virtual void accept(Visitor* visitor) = 0;
};

class Circle : public Element {
public:
    void accept(Visitor* visitor) override;
    void draw() { std::cout << "Drawing circle\n"; }
};

class Rectangle : public Element {
public:
    void accept(Visitor* visitor) override;
    void draw() { std::cout << "Drawing rectangle\n"; }
};

class Visitor {
public:
    virtual ~Visitor() = default;
    virtual void visit(Circle* c) = 0;
    virtual void visit(Rectangle* r) = 0;
};

void Circle::accept(Visitor* visitor) {
    visitor->visit(this);
}

void Rectangle::accept(Visitor* visitor) {
    visitor->visit(this);
}

class DrawVisitor : public Visitor {
public:
    void visit(Circle* c) override {
        c->draw();
    }
    
    void visit(Rectangle* r) override {
        r->draw();
    }
};

int main() {
    auto circle = std::make_shared<Circle>();
    auto rectangle = std::make_shared<Rectangle>();
    auto visitor = std::make_shared<DrawVisitor>();
    
    circle->accept(visitor.get());
    rectangle->accept(visitor.get());
}
