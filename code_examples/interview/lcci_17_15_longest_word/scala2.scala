object Solution {
  def longestWord(words: Array[String]): String = {
    val wordSet = scala.collection.mutable.Set(words: _*)

    def canBuild(w: String): Boolean = {
      if (w.isEmpty) return true
      (1 to w.length).exists(i => wordSet.contains(w.take(i)) && canBuild(w.drop(i)))
    }

    val sorted = words.sortWith((a, b) => if (a.length != b.length) a.length > b.length else a < b)
    for (w <- sorted) {
      wordSet.remove(w)
      if (canBuild(w)) return w
      wordSet.add(w)
    }
    ""
  }
}
