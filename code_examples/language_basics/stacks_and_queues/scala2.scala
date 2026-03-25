import scala.collection.mutable

object StacksAndQueues {
  def main(args: Array[String]): Unit = {
    val stack = mutable.Stack[Int]()
    List(1, 2, 3).foreach(stack.push)
    println(s"stack top: ${stack.top}")  // 3 (LIFO)
    stack.pop()
    println(s"after pop: ${stack.top}")  // 2

    val queue = mutable.Queue[Int]()
    List(1, 2, 3).foreach(queue.enqueue)
    println(s"queue front: ${queue.front}")  // 1 (FIFO)
    queue.dequeue()
    println(s"after dequeue: ${queue.front}")  // 2
  }
}
