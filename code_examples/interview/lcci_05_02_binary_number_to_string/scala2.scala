object Lcci0502BinaryNumberToString {
  def binaryToString(n0: Double): String = {
    val sb = new StringBuilder("0.")
    var n = n0
    while (n > 0) {
      if (sb.length > 32) return "ERROR"
      n *= 2
      if (n >= 1) { sb.append('1'); n -= 1 }
      else sb.append('0')
    }
    sb.toString
  }

  def main(args: Array[String]): Unit = {
    println(binaryToString(0.625))
    println(binaryToString(0.1))
  }
}
