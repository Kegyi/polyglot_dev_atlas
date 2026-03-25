object Lcci0304QueueViaStacks {
  final class MyQueue {
    private val inStack = scala.collection.mutable.ArrayBuffer.empty[Int]
    private val outStack = scala.collection.mutable.ArrayBuffer.empty[Int]

    def push(x: Int): Unit = inStack += x

    private def moveIfNeeded(): Unit = {
      if (outStack.nonEmpty) return
      while (inStack.nonEmpty) {
        outStack += inStack.remove(inStack.length - 1)
      }
    }

    def pop(): Int = {
      moveIfNeeded()
      if (outStack.isEmpty) -1 else outStack.remove(outStack.length - 1)
    }

    def peek(): Int = {
      moveIfNeeded()
      if (outStack.isEmpty) -1 else outStack.last
    }

    def empty(): Boolean = inStack.isEmpty && outStack.isEmpty
  }

  def main(args: Array[String]): Unit = {
    val q = new MyQueue
    q.push(1)
    q.push(2)
    q.push(3)
    println(q.peek())
    println(q.pop())
    println(q.pop())
    println(q.empty())
  }
}
