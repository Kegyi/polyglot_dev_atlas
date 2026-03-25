object Lcci0504ClosedNumber {
  def findClosedNumbers(num: Int): (Int, Int) = {
    var bigger = num
    var smaller = num

    var i = 1
    while (i < 32) {
      if ((bigger >> (i - 1) & 1) == 1 && (bigger >> i & 1) == 0) {
        bigger |= 1 << i; bigger &= ~(1 << (i - 1)); i = 32
      }
      i += 1
    }

    i = 1
    while (i < 32) {
      if ((smaller >> (i - 1) & 1) == 0 && (smaller >> i & 1) == 1) {
        smaller &= ~(1 << i); smaller |= 1 << (i - 1); i = 32
      }
      i += 1
    }

    (bigger, smaller)
  }

  def main(args: Array[String]): Unit = {
    val (bigger, smaller) = findClosedNumbers(2)
    println(bigger)
    println(smaller)
  }
}
