object BitManipulation {
  def countBits(n: Int): Int = {
    var count = 0
    var x = n
    while (x != 0) { count += x & 1; x >>= 1 }
    count
  }

  def main(args: Array[String]): Unit = {
    val a = 10  // 1010 in binary
    val b = 12  // 1100 in binary
    println(s"a & b:  ${(a & b).toBinaryString}")  // 1000
    println(s"a | b:  ${(a | b).toBinaryString}")  // 1110
    println(s"a ^ b:  ${(a ^ b).toBinaryString}")  // 110

    var n = 5   // 0101 in binary
    println(s"bit 1 set? ${(n >> 1) & 1}")  // check -> 0
    n |= (1 << 2)    // set bit 2
    n &= ~(1 << 0)   // clear bit 0
    println(s"after set/clear: ${n.toBinaryString}")  // 100

    println(s"count bits in 7: ${countBits(7)}")  // 3
  }
}
