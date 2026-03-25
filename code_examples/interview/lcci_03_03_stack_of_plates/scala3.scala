object Lcci0303StackOfPlates:
  final class StackOfPlates(capacity: Int) {
    private val stacks = scala.collection.mutable.ArrayBuffer.empty[scala.collection.mutable.ArrayBuffer[Int]]

    def push(value: Int): Unit =
      if (capacity <= 0) return
      if (stacks.isEmpty || stacks.last.length == capacity) {
        stacks += scala.collection.mutable.ArrayBuffer.empty[Int]
      }
      stacks.last += value

    def pop(): Int = popAt(stacks.length - 1)

    def popAt(index: Int): Int =
      if (index < 0 || index >= stacks.length || stacks(index).isEmpty) return -1
      val value = stacks(index).remove(stacks(index).length - 1)
      if (stacks(index).isEmpty) stacks.remove(index)
      value
  }

  @main def main(): Unit =
    val s = new StackOfPlates(2)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    println(s.popAt(0))
    println(s.pop())
    println(s.pop())
    println(s.pop())
