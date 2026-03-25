object Lcci0404CheckBalance {
  final case class Node(value: Int, var left: Node | Null = null, var right: Node | Null = null)

  def heightOrFail(n: Node | Null): Int = {
    if (n == null) return 0
    val lh = heightOrFail(n.asInstanceOf[Node].left)
    if (lh == -1) return -1
    val rh = heightOrFail(n.asInstanceOf[Node].right)
    if (rh == -1) return -1
    if (math.abs(lh - rh) > 1) return -1
    1 + math.max(lh, rh)
  }

  def isBalanced(root: Node | Null): Boolean = heightOrFail(root) != -1

  def main(args: Array[String]): Unit = {
    val a = Node(1, Node(2), Node(3))
    val b = Node(1, Node(2, Node(3, Node(4), null), null), null)
    println(isBalanced(a))
    println(isBalanced(b))
  }
}
