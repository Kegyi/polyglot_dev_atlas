import scala.collection.mutable

object Lcci0401RouteBetweenNodes {
  def hasRoute(n: Int, edges: Vector[(Int, Int)], start: Int, target: Int): Boolean = {
    val g = Array.fill(n)(mutable.ArrayBuffer.empty[Int])
    edges.foreach { case (u, v) => g(u) += v }
    val seen = Array.fill(n)(false)
    val q = mutable.Queue(start)
    seen(start) = true
    while (q.nonEmpty) {
      val u = q.dequeue()
      if (u == target) return true
      g(u).foreach { v => if (!seen(v)) { seen(v) = true; q.enqueue(v) } }
    }
    false
  }

  def main(args: Array[String]): Unit = {
    val edges = Vector((0, 1), (0, 2), (1, 3), (2, 4))
    println(hasRoute(5, edges, 0, 4))
    println(hasRoute(5, edges, 3, 4))
  }
}
