object Lcci0503FlipBitToWin:
  def flipBit(num: Int): Int =
    if (~num == 0) return 32
    var n = num & 0xFFFFFFFFL.toInt
    // Use unsigned right shift via Long
    var uNum = num.toLong & 0xFFFFFFFFL
    var cur = 0; var prev = 0; var best = 1
    while (uNum > 0) {
      if ((uNum & 1) == 1) cur += 1
      else { prev = cur; cur = 0 }
      val v = prev + 1 + cur
      if (v > best) best = v
      uNum >>>= 1
    }
    best

  @main def main(): Unit =
    println(flipBit(1775))
    println(flipBit(7))
