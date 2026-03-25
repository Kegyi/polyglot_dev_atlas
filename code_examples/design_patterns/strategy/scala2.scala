// Strategy
trait Strategy {
    def execute(a: Int, b: Int): Int
}

class AddStrategy extends Strategy {
    def execute(a: Int, b: Int): Int = a + b
}

class SubtractStrategy extends Strategy {
    def execute(a: Int, b: Int): Int = a - b
}

class MultiplyStrategy extends Strategy {
    def execute(a: Int, b: Int): Int = a * b
}

class Context(private var strategy: Strategy) {
    def setStrategy(s: Strategy): Unit = {
        strategy = s
    }
    
    def executeStrategy(a: Int, b: Int): Int = {
        strategy.execute(a, b)
    }
}

object Main extends App {
    val ctx = new Context(new AddStrategy())
    
    println(s"Add: ${ctx.executeStrategy(5, 3)}")
    
    ctx.setStrategy(new SubtractStrategy())
    println(s"Subtract: ${ctx.executeStrategy(5, 3)}")
    
    ctx.setStrategy(new MultiplyStrategy())
    println(s"Multiply: ${ctx.executeStrategy(5, 3)}")
}
