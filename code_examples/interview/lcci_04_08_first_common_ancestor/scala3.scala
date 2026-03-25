object Lcci0408FirstCommonAncestor:
  final case class Node(value: Int, var left: Node | Null = null, var right: Node | Null = null)

  def lca(root: Node | Null, p: Int, q: Int): Node | Null =
    if (root == null) return null
    val cur = root.asInstanceOf[Node]
    if (cur.value == p || cur.value == q) return cur
    val left = lca(cur.left, p, q)
    val right = lca(cur.right, p, q)
    if (left != null && right != null) cur else if (left != null) left else right

  @main def main(): Unit =
    val root = Node(3,
      Node(5, Node(6), Node(2)),
      Node(1, Node(0), Node(8))
    )
    println(lca(root, 6, 2).asInstanceOf[Node].value)
    println(lca(root, 6, 8).asInstanceOf[Node].value)
