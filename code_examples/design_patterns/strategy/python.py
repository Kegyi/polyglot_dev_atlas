from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute(self, a: int, b: int) -> int:
        pass

class AddStrategy(Strategy):
    def execute(self, a: int, b: int) -> int:
        return a + b

class SubtractStrategy(Strategy):
    def execute(self, a: int, b: int) -> int:
        return a - b

class MultiplyStrategy(Strategy):
    def execute(self, a: int, b: int) -> int:
        return a * b

class Context:
    def __init__(self):
        self.strategy: Strategy = None
    
    def set_strategy(self, strategy: Strategy) -> None:
        self.strategy = strategy
    
    def execute_strategy(self, a: int, b: int) -> int:
        return self.strategy.execute(a, b)

ctx = Context()

ctx.set_strategy(AddStrategy())
print(f"Add: {ctx.execute_strategy(5, 3)}")

ctx.set_strategy(SubtractStrategy())
print(f"Subtract: {ctx.execute_strategy(5, 3)}")

ctx.set_strategy(MultiplyStrategy())
print(f"Multiply: {ctx.execute_strategy(5, 3)}")
