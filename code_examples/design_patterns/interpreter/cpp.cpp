#include <iostream>
#include <string>
#include <memory>

class Expression {
public:
    virtual ~Expression() = default;
    virtual bool interpret(const std::string& ctx) = 0;
};

class TerminalExpression : public Expression {
private:
    std::string literal;
public:
    TerminalExpression(const std::string& lit) : literal(lit) {}
    
    bool interpret(const std::string& ctx) override {
        return ctx.find(literal) != std::string::npos;
    }
};

class OrExpression : public Expression {
private:
    std::shared_ptr<Expression> expr1, expr2;
public:
    OrExpression(std::shared_ptr<Expression> e1, std::shared_ptr<Expression> e2)
        : expr1(e1), expr2(e2) {}
    
    bool interpret(const std::string& ctx) override {
        return expr1->interpret(ctx) || expr2->interpret(ctx);
    }
};

class AndExpression : public Expression {
private:
    std::shared_ptr<Expression> expr1, expr2;
public:
    AndExpression(std::shared_ptr<Expression> e1, std::shared_ptr<Expression> e2)
        : expr1(e1), expr2(e2) {}
    
    bool interpret(const std::string& ctx) override {
        return expr1->interpret(ctx) && expr2->interpret(ctx);
    }
};

int main() {
    auto c1 = std::make_shared<TerminalExpression>("cat");
    auto c2 = std::make_shared<TerminalExpression>("dog");
    auto expr = std::make_shared<OrExpression>(c1, c2);
    
    std::cout << (expr->interpret("cat") ? "true" : "false") << std::endl;
    std::cout << (expr->interpret("bird") ? "true" : "false") << std::endl;
}
