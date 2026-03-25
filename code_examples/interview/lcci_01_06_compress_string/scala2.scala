object Lcci0106CompressString {
  def compressString(s: String): String = {
    if (s.isEmpty) {
      return s
    }

    val b = new StringBuilder
    var run = 1

    for (i <- 1 to s.length) {
      if (i < s.length && s(i) == s(i - 1)) {
        run += 1
      } else {
        b.append(s(i - 1))
        b.append(run)
        run = 1
      }
    }

    val compressed = b.toString()
    if (compressed.length < s.length) compressed else s
  }

  def main(args: Array[String]): Unit = {
    println(s"aabcccccaaa -> ${compressString("aabcccccaaa")}")
    println(s"abbccd -> ${compressString("abbccd")}")
  }
}
