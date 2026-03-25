object FunctionsAndErrorsBasics:
  def add(a: Int, b: Int): Int = a + b

  def safeDiv(a: Double, b: Double): Option[Double] =
    if (b == 0) None else Some(a / b)

  def strictDiv(a: Double, b: Double): Double =
    if (b == 0) throw new IllegalArgumentException("division by zero")
    a / b

  @main def main(): Unit =
    println(s"add(2, 3): ${add(2, 3)}")
    println(s"safeDiv(10, 2): ${safeDiv(10, 2)}")

    try {
      println(s"strictDiv(10, 0): ${strictDiv(10, 0)}")
    } catch {
      case ex: IllegalArgumentException => println(s"error: ${ex.getMessage}")
    }
