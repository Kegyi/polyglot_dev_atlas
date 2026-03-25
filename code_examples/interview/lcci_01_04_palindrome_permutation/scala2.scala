object Lcci0104PalindromePermutation {
  def canPermutePalindrome(s: String): Boolean = {
    val freq = scala.collection.mutable.Map.empty[Char, Int].withDefaultValue(0)

    s.toLowerCase.foreach { ch =>
      if (!ch.isWhitespace) {
        freq.update(ch, freq(ch) + 1)
      }
    }

    freq.values.count(_ % 2 == 1) <= 1
  }

  def main(args: Array[String]): Unit = {
    println(s"tact coa -> ${canPermutePalindrome("tact coa")}")
    println(s"daily -> ${canPermutePalindrome("daily")}")
  }
}
