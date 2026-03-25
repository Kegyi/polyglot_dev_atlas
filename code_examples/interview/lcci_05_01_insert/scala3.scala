object Lcci0501Insert:
  def insert(N: Int, M: Int, i: Int, j: Int): Int =
    val mask = ~(((1 << (j - i + 1)) - 1) << i)
    (N & mask) | (M << i)

  @main def main(): Unit =
    println(insert(1024, 19, 2, 6))
    println(insert(0, 19, 0, 4))
