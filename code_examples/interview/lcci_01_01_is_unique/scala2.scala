object Lcci0101IsUnique {
  def isUnique(s: String): Boolean = {
    val seen = scala.collection.mutable.HashSet.empty[Char]
    s.forall { ch =>
      if (seen.contains(ch)) {
        false
      } else {
        seen += ch
        true
      }
    }
  }

  def main(args: Array[String]): Unit = {
    println(s"leetcode -> ${isUnique("leetcode")}")
    println(s"abc -> ${isUnique("abc")}")
  }
}
