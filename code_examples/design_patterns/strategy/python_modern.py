# Modern Python Strategy using plain callables
# No Strategy ABC or subclasses - any callable with the right signature works.
from typing import Callable

Strategy = Callable[[int, int], int]

class Calculator:
    def __init__(self, strategy: Strategy) -> None:
        self.strategy = strategy

    def execute(self, a: int, b: int) -> int:
        return self.strategy(a, b)

# Named functions, lambdas, or method references all slot in directly
calc = Calculator(lambda a, b: a + b)
print(f"Add: {calc.execute(5, 3)}")

calc.strategy = lambda a, b: a - b
print(f"Subtract: {calc.execute(5, 3)}")

calc.strategy = lambda a, b: a * b
print(f"Multiply: {calc.execute(5, 3)}")
