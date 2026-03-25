#include <iostream>
#include <memory>

class Strategy {
public:
    virtual ~Strategy() = default;
    virtual int execute(int a, int b) = 0;
};

class AddStrategy : public Strategy {
public:
    int execute(int a, int b) override {
        return a + b;
    }
};

class SubtractStrategy : public Strategy {
public:
    int execute(int a, int b) override {
        return a - b;
    }
};

class MultiplyStrategy : public Strategy {
public:
    int execute(int a, int b) override {
        return a * b;
    }
};

class Context {
private:
    std::shared_ptr<Strategy> strategy;
public:
    void setStrategy(std::shared_ptr<Strategy> s) { strategy = s; }
    int executeStrategy(int a, int b) { return strategy->execute(a, b); }
};

int main() {
    Context ctx;
    
    ctx.setStrategy(std::make_shared<AddStrategy>());
    std::cout << "Add: " << ctx.executeStrategy(5, 3) << std::endl;
    
    ctx.setStrategy(std::make_shared<SubtractStrategy>());
    std::cout << "Subtract: " << ctx.executeStrategy(5, 3) << std::endl;
    
    ctx.setStrategy(std::make_shared<MultiplyStrategy>());
    std::cout << "Multiply: " << ctx.executeStrategy(5, 3) << std::endl;
}
