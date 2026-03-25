object Solution {
  def respace(dictionary: Array[String], sentence: String): Int = {
    val s = dictionary.toSet
    val n = sentence.length
    val dp = Array.fill(n + 1)(0)
    for (i <- 1 to n) {
      dp(i) = dp(i - 1) + 1
      for (j <- 0 until i) {
        if (s.contains(sentence.substring(j, i))) {
          dp(i) = dp(i).min(dp(j))
        }
      }
    }
    dp(n)
  }
}
