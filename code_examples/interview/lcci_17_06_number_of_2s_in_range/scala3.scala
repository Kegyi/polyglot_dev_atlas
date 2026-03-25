object Lcci1706NumberOf2sInRange:
  def numberOf2sInRange(n: Int): Int =
    var count = 0
    var m = 1
    while (m <= n) {
      val a = n / m
      val b = n % m
      val digit = a % 10
      if (digit > 2) count += (a / 10 + 1) * m
      else if (digit == 2) count += (a / 10) * m + b + 1
      else count += (a / 10) * m
      m *= 10
    }
    count

  @main def main(): Unit =
    println(numberOf2sInRange(25)) // 9
    println(numberOf2sInRange(20)) // 2
