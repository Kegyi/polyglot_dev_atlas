import scala.collection.mutable

object TreesAndGraphs:
  case class TreeNode(value: Int, var left: Option[TreeNode] = None, var right: Option[TreeNode] = None)

  def insert(root: Option[TreeNode], value: Int): TreeNode = root match {
    case None => TreeNode(value)
    case Some(node) =>
      if (value < node.value) node.left  = Some(insert(node.left,  value))
      else                    node.right = Some(insert(node.right, value))
      node
  }

  def inOrder(root: Option[TreeNode]): List[Int] = root match {
    case None       => Nil
    case Some(node) => inOrder(node.left) ::: node.value :: inOrder(node.right)
  }

  def bfs(root: Option[TreeNode]): List[Int] =
    val queue  = mutable.Queue[TreeNode]()
    val result = mutable.ListBuffer[Int]()
    root.foreach(queue.enqueue)
    while (queue.nonEmpty) {
      val node = queue.dequeue()
      result += node.value
      node.left.foreach(queue.enqueue)
      node.right.foreach(queue.enqueue)
    }
    result.toList

  @main def main(): Unit =
    var root: Option[TreeNode] = None
    for (v <- List(5, 3, 7, 1, 4)) root = Some(insert(root, v))
    println(s"in-order: ${inOrder(root)}")  // List(1, 3, 4, 5, 7)
    println(s"bfs:      ${bfs(root)}")      // List(5, 3, 7, 1, 4)
