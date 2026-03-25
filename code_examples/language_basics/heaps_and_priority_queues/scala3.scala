import scala.collection.mutable

object HeapsAndPriorityQueues:
  @main def main(): Unit =
    val data = List(3, 1, 4, 1, 5, 9)

    // max priority queue (default)
    val maxPQ = mutable.PriorityQueue[Int]()
    data.foreach(maxPQ.enqueue)
    println(s"max: ${maxPQ.head}")  // 9

    // min priority queue via reverse ordering
    val minPQ = mutable.PriorityQueue[Int]()(Ordering[Int].reverse)
    data.foreach(minPQ.enqueue)
    print("drain min-heap: ")
    while (minPQ.nonEmpty) print(s"${minPQ.dequeue()} ")
    println()  // 1 1 3 4 5 9
