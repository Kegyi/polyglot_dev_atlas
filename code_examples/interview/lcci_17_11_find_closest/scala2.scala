object Lcci1711FindClosest {
  def findClosest(words: Array[String], word1: String, word2: String): Int = {
    var i1 = -1
    var i2 = -1
    var ans = Int.MaxValue
    for (i <- words.indices) {
      if (words(i) == word1) i1 = i
      if (words(i) == word2) i2 = i
      if (i1 != -1 && i2 != -1) ans = math.min(ans, math.abs(i1 - i2))
    }
    ans
  }

  def main(args: Array[String]): Unit = {
    println(findClosest(Array("I", "am", "a", "student", "from", "a", "university", "in", "a", "city"), "a", "student")) // 1
    println(findClosest(Array("aa", "bb"), "aa", "bb")) // 1
  }
}
