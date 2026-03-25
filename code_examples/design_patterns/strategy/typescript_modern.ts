// Modern TypeScript Strategy using function types
// No Strategy interface or class hierarchy - strategies are plain function values.

type Strategy = (a: number, b: number) => number;

class Calculator {
    constructor(public strategy: Strategy) {}

    execute(a: number, b: number): number {
        return this.strategy(a, b);
    }
}

let calc = new Calculator((a, b) => a + b);
console.log("Add:", calc.execute(5, 3));

calc.strategy = (a, b) => a - b;
console.log("Subtract:", calc.execute(5, 3));

calc.strategy = (a, b) => a * b;
console.log("Multiply:", calc.execute(5, 3));
