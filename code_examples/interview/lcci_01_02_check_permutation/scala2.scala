object Lcci0102CheckPermutation {
  def checkPermutation(a: String, b: String): Boolean = {
    if (a.length != b.length) {
      return false
    }

    val freq = Array.fill(256)(0)
    a.foreach(ch => freq(ch) += 1)

    b.foreach { ch =>
      freq(ch) -= 1
      if (freq(ch) < 0) {
        return false
      }
    }

    true
  }

  def main(args: Array[String]): Unit = {
    println(s"abcde vs edcba -> ${checkPermutation("abcde", "edcba")}")
    println(s"abc vs abz -> ${checkPermutation("abc", "abz")}")
  }
}
