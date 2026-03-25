// Modern Scala Strategy using function values and Scala 3 type classes (given/using)
// No Strategy trait or subclasses - strategies are plain function values.

// Approach 1: function value (simplest)
class Calculator(val strategy: (Int, Int) => Int):
  def execute(a: Int, b: Int): Int = strategy(a, b)

// Approach 2: type class with given/using (Scala 3) - zero-overhead, compile-time resolved
trait Strategy:
  def execute(a: Int, b: Int): Int

given addStrategy: Strategy with
  def execute(a: Int, b: Int) = a + b

given subtractStrategy: Strategy with
  def execute(a: Int, b: Int) = a - b

def calculate(a: Int, b: Int)(using s: Strategy): Int = s.execute(a, b)

@main def strategyModernExample(): Unit =
  // Function value approach
  val add  = Calculator(_ + _)
  val sub  = Calculator(_ - _)
  val mul  = Calculator(_ * _)
  println(s"Add: ${add.execute(5, 3)}")
  println(s"Subtract: ${sub.execute(5, 3)}")
  println(s"Multiply: ${mul.execute(5, 3)}")

  // Type class approach
  println(s"Given add: ${calculate(5, 3)(using addStrategy)}")
  println(s"Given sub: ${calculate(5, 3)(using subtractStrategy)}")
