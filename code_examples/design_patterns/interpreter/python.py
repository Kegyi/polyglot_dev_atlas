from abc import ABC, abstractmethod

class Expression(ABC):
    @abstractmethod
    def interpret(self, ctx: str) -> bool:
        pass

class TerminalExpression(Expression):
    def __init__(self, literal: str):
        self.literal = literal
    
    def interpret(self, ctx: str) -> bool:
        return self.literal in ctx

class OrExpression(Expression):
    def __init__(self, expr1: Expression, expr2: Expression):
        self.expr1 = expr1
        self.expr2 = expr2
    
    def interpret(self, ctx: str) -> bool:
        return self.expr1.interpret(ctx) or self.expr2.interpret(ctx)

class AndExpression(Expression):
    def __init__(self, expr1: Expression, expr2: Expression):
        self.expr1 = expr1
        self.expr2 = expr2
    
    def interpret(self, ctx: str) -> bool:
        return self.expr1.interpret(ctx) and self.expr2.interpret(ctx)

c1 = TerminalExpression("cat")
c2 = TerminalExpression("dog")
expr = OrExpression(c1, c2)

print(expr.interpret("cat"))
print(expr.interpret("bird"))
