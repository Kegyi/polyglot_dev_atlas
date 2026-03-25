object Lcci0406Successor:
  final case class Node(value: Int, var left: Node | Null = null, var right: Node | Null = null)

  def inorderSuccessor(root0: Node | Null, p: Int): Node | Null =
    var root = root0
    var ans: Node | Null = null
    while (root != null) {
      val cur = root.asInstanceOf[Node]
      if (p < cur.value) {
        ans = cur
        root = cur.left
      } else {
        root = cur.right
      }
    }
    ans

  @main def main(): Unit =
    val root = Node(5, Node(3, Node(2), Node(4)), Node(7))
    val s1 = inorderSuccessor(root, 3)
    val s2 = inorderSuccessor(root, 7)
    println(if (s1 == null) -1 else s1.asInstanceOf[Node].value)
    println(if (s2 == null) -1 else s2.asInstanceOf[Node].value)
