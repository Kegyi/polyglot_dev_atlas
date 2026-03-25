object Lcci0412PathsWithSum {
  final case class Node(value: Int, var left: Node | Null = null, var right: Node | Null = null)

  def pathSum(root: Node | Null, target: Int): Int = {
    val counts = scala.collection.mutable.Map[Long, Int](0L -> 1)

    def dfs(node: Node | Null, prefix: Long): Int = {
      if (node == null) return 0
      val cur = node.asInstanceOf[Node]
      val next = prefix + cur.value
      var res = counts.getOrElse(next - target, 0)
      counts.update(next, counts.getOrElse(next, 0) + 1)
      res += dfs(cur.left, next)
      res += dfs(cur.right, next)
      counts.update(next, counts(next) - 1)
      res
    }

    dfs(root, 0L)
  }

  def main(args: Array[String]): Unit = {
    val root = Node(
      10,
      Node(5, Node(3, Node(3), Node(-2)), Node(2, null, Node(1))),
      Node(-3, null, Node(11))
    )
    println(pathSum(root, 8))
  }
}
