object Lcci0410CheckSubtree {
  final case class Node(value: Int, var left: Node | Null = null, var right: Node | Null = null)

  def same(a: Node | Null, b: Node | Null): Boolean = {
    if (a == null && b == null) return true
    if (a == null || b == null) return false
    val x = a.asInstanceOf[Node]
    val y = b.asInstanceOf[Node]
    x.value == y.value && same(x.left, y.left) && same(x.right, y.right)
  }

  def isSubtree(t1: Node | Null, t2: Node | Null): Boolean = {
    if (t2 == null) return true
    if (t1 == null) return false
    val cur = t1.asInstanceOf[Node]
    same(cur, t2) || isSubtree(cur.left, t2) || isSubtree(cur.right, t2)
  }

  def main(args: Array[String]): Unit = {
    val t1 = Node(3, Node(4, Node(1), Node(2)), Node(5))
    val t2 = Node(4, Node(1), Node(2))
    val t3 = Node(4, Node(1), Node(3))
    println(isSubtree(t1, t2))
    println(isSubtree(t1, t3))
  }
}
