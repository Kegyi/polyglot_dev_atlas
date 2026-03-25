import scala.collection.mutable

object Lcci0403ListOfDepth:
  final case class Node(value: Int, var left: Node | Null = null, var right: Node | Null = null)

  def listOfDepth(root: Node | Null): Vector[Vector[Int]] =
    if (root == null) return Vector.empty
    val q = mutable.Queue(root.asInstanceOf[Node])
    val out = mutable.ArrayBuffer.empty[Vector[Int]]
    while (q.nonEmpty) {
      val n = q.size
      val level = mutable.ArrayBuffer.empty[Int]
      (0 until n).foreach { _ =>
        val cur = q.dequeue()
        level += cur.value
        if (cur.left != null) q.enqueue(cur.left.asInstanceOf[Node])
        if (cur.right != null) q.enqueue(cur.right.asInstanceOf[Node])
      }
      out += level.toVector
    }
    out.toVector

  @main def main(): Unit =
    val root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
    println(listOfDepth(root).map(_.mkString(" ")).mkString(" | "))
