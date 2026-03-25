import scala.collection.mutable

object Solution {
  class TrieNode {
    val children: Array[TrieNode] = new Array[TrieNode](26)
    var idx: Int = -1
  }

  def multiSearch(big: String, smalls: Array[String]): Array[Array[Int]] = {
    val root = new TrieNode()
    for ((s, i) <- smalls.zipWithIndex if s.nonEmpty) {
      var node = root
      for (c <- s) {
        val j = c - 'a'
        if (node.children(j) == null) node.children(j) = new TrieNode()
        node = node.children(j)
      }
      node.idx = i
    }
    val ans = Array.fill(smalls.length)(mutable.ArrayBuffer[Int]())
    for (i <- big.indices) {
      var node = root
      var j = i
      var stop = false
      while (j < big.length && !stop) {
        val k = big(j) - 'a'
        if (node.children(k) == null) stop = true
        else {
          node = node.children(k)
          if (node.idx != -1) ans(node.idx) += i
          j += 1
        }
      }
    }
    ans.map(_.toArray)
  }
}
