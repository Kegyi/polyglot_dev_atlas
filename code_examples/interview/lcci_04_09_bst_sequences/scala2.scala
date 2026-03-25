object Lcci0409BstSequences {
  final case class Node(value: Int, left: Node | Null = null, right: Node | Null = null)

  def weave(first: List[Int], second: List[Int], prefix: List[Int]): List[List[Int]] = {
    if (first.isEmpty || second.isEmpty) return List(prefix ++ first ++ second)
    val withFirst = weave(first.tail, second, prefix :+ first.head)
    val withSecond = weave(first, second.tail, prefix :+ second.head)
    withFirst ++ withSecond
  }

  def allSeq(root: Node | Null): List[List[Int]] = {
    if (root == null) return List(Nil)
    val cur = root.asInstanceOf[Node]
    val left = allSeq(cur.left)
    val right = allSeq(cur.right)

    for {
      l <- left
      r <- right
      w <- weave(l, r, List(cur.value))
    } yield w
  }

  def main(args: Array[String]): Unit = {
    val root = Node(2, Node(1), Node(3))
    allSeq(root).foreach(seq => println(seq.mkString(" ")))
  }
}
