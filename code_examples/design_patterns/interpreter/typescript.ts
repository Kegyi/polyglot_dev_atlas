interface Expression {
    interpret(ctx: string): boolean;
}

class TerminalExpression implements Expression {
    constructor(private literal: string) {}
    
    interpret(ctx: string): boolean {
        return ctx.includes(this.literal);
    }
}

class OrExpression implements Expression {
    constructor(private expr1: Expression, private expr2: Expression) {}
    
    interpret(ctx: string): boolean {
        return this.expr1.interpret(ctx) || this.expr2.interpret(ctx);
    }
}

class AndExpression implements Expression {
    constructor(private expr1: Expression, private expr2: Expression) {}
    
    interpret(ctx: string): boolean {
        return this.expr1.interpret(ctx) && this.expr2.interpret(ctx);
    }
}

const c1 = new TerminalExpression("cat");
const c2 = new TerminalExpression("dog");
const expr = new OrExpression(c1, c2);

console.log(expr.interpret("cat"));
console.log(expr.interpret("bird"));
