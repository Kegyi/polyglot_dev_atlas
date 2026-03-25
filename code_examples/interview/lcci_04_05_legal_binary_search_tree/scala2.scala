object Lcci0405LegalBinarySearchTree {
  final case class Node(value: Int, var left: Node | Null = null, var right: Node | Null = null)

  def isValid(n: Node | Null, lo: Long, hi: Long): Boolean = {
    if (n == null) return true
    val v = n.asInstanceOf[Node].value.toLong
    if (v <= lo || v >= hi) return false
    isValid(n.asInstanceOf[Node].left, lo, v) && isValid(n.asInstanceOf[Node].right, v, hi)
  }

  def main(args: Array[String]): Unit = {
    val ok = Node(5, Node(3), Node(7))
    val bad = Node(5, Node(3, null, Node(6)), Node(7))
    println(isValid(ok, Long.MinValue, Long.MaxValue))
    println(isValid(bad, Long.MinValue, Long.MaxValue))
  }
}
