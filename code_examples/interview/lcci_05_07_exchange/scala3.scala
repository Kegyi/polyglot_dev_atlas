object Lcci0507Exchange:
  def exchangeBits(num: Int): Int =
    val u = num & 0xFFFFFFFFL
    val odd  = (u & 0xAAAAAAAAL) >> 1
    val even = (u & 0x55555555L) << 1
    (odd | even).toInt

  @main def main(): Unit =
    println(exchangeBits(2))
    println(exchangeBits(3))
