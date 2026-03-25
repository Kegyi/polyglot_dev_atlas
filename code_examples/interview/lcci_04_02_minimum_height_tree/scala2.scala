object Lcci0402MinimumHeightTree {
  final case class Node(value: Int, var left: Node | Null = null, var right: Node | Null = null)

  def build(nums: Vector[Int], lo: Int, hi: Int): Node | Null = {
    if (lo > hi) return null
    val mid = (lo + hi) / 2
    val root = Node(nums(mid))
    root.left = build(nums, lo, mid - 1)
    root.right = build(nums, mid + 1, hi)
    root
  }

  def inorder(n: Node | Null, out: scala.collection.mutable.ArrayBuffer[Int]): Unit = {
    if (n == null) return
    inorder(n.asInstanceOf[Node].left, out)
    out += n.asInstanceOf[Node].value
    inorder(n.asInstanceOf[Node].right, out)
  }

  def main(args: Array[String]): Unit = {
    val nums = Vector(1, 2, 3, 4, 5, 6, 7)
    val root = build(nums, 0, nums.length - 1)
    val out = scala.collection.mutable.ArrayBuffer.empty[Int]
    inorder(root, out)
    println(out.mkString(" "))
  }
}
