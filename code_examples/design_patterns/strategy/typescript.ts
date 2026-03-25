interface IStrategy {
    execute(a: number, b: number): number;
}

class AddStrategy implements IStrategy {
    execute(a: number, b: number): number {
        return a + b;
    }
}

class SubtractStrategy implements IStrategy {
    execute(a: number, b: number): number {
        return a - b;
    }
}

class MultiplyStrategy implements IStrategy {
    execute(a: number, b: number): number {
        return a * b;
    }
}

class Context {
    private strategy: IStrategy;
    
    setStrategy(strategy: IStrategy): void {
        this.strategy = strategy;
    }
    
    executeStrategy(a: number, b: number): number {
        return this.strategy.execute(a, b);
    }
}

const ctx = new Context();

ctx.setStrategy(new AddStrategy());
console.log(`Add: ${ctx.executeStrategy(5, 3)}`);

ctx.setStrategy(new SubtractStrategy());
console.log(`Subtract: ${ctx.executeStrategy(5, 3)}`);

ctx.setStrategy(new MultiplyStrategy());
console.log(`Multiply: ${ctx.executeStrategy(5, 3)}`);
