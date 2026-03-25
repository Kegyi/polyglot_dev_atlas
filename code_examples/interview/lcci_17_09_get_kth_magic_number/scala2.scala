object Lcci1709GetKthMagicNumber {
  def getKthMagicNumber(k: Int): Int = {
    val dp = Array.fill(k + 1)(0)
    dp(1) = 1
    var i3 = 1
    var i5 = 1
    var i7 = 1
    for (i <- 2 to k) {
      val a = dp(i3) * 3
      val b = dp(i5) * 5
      val c = dp(i7) * 7
      dp(i) = math.min(a, math.min(b, c))
      if (dp(i) == a) i3 += 1
      if (dp(i) == b) i5 += 1
      if (dp(i) == c) i7 += 1
    }
    dp(k)
  }

  def main(args: Array[String]): Unit = {
    println(getKthMagicNumber(5)) // 9
    println(getKthMagicNumber(1)) // 1
  }
}
