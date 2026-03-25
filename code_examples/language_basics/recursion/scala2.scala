object RecursionBasics {
  def factorial(n: Int): Int = {
    if (n <= 1) 1 else n * factorial(n - 1)
  }

  def sumRecursive(values: Vector[Int], index: Int = 0): Int = {
    if (index >= values.length) 0
    else values(index) + sumRecursive(values, index + 1)
  }

  def main(args: Array[String]): Unit = {
    val values = Vector(1, 2, 3, 4)
    println(s"factorial(5): ${factorial(5)}")
    println(s"sumRecursive(values): ${sumRecursive(values)}")
  }
}
