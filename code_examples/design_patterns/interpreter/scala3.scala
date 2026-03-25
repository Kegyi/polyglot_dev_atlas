// Interpreter
trait Expression:
    def interpret(ctx: String): Boolean

class TerminalExpression(literal: String) extends Expression:
    def interpret(ctx: String): Boolean = ctx.contains(literal)

class OrExpression(expr1: Expression, expr2: Expression) extends Expression:
    def interpret(ctx: String): Boolean = expr1.interpret(ctx) || expr2.interpret(ctx)

class AndExpression(expr1: Expression, expr2: Expression) extends Expression:
    def interpret(ctx: String): Boolean = expr1.interpret(ctx) && expr2.interpret(ctx)

@main def main(): Unit =
    val c1: Expression = new TerminalExpression("cat")
    val c2: Expression = new TerminalExpression("dog")
    val expr: Expression = new OrExpression(c1, c2)
    
    println(expr.interpret("cat"))
    println(expr.interpret("bird"))
