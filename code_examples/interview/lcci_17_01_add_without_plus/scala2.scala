object Lcci1701AddWithoutPlus {
  def add(a: Int, b: Int): Int = {
    var x = a
    var y = b
    while (y != 0) {
      val carry = (x & y) << 1
      x = x ^ y
      y = carry
    }
    x
  }

  def main(args: Array[String]): Unit = {
    println(add(1, 2))    // 3
    println(add(3, -2))   // 1
    println(add(-1, -2))  // -3
  }
}
