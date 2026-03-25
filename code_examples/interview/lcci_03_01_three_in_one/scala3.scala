object Lcci0301ThreeInOne:
  final class TripleInOne(stackSize: Int) {
    private val size = stackSize
    private val data = Array.fill(3 * stackSize)(0)
    private val tops = Array(0, 0, 0)

    def push(stackNum: Int, value: Int): Unit =
      if (tops(stackNum) == size) return
      val index = stackNum * size + tops(stackNum)
      data(index) = value
      tops(stackNum) += 1

    def pop(stackNum: Int): Int =
      if (tops(stackNum) == 0) return -1
      tops(stackNum) -= 1
      val index = stackNum * size + tops(stackNum)
      data(index)

    def peek(stackNum: Int): Int =
      if (tops(stackNum) == 0) return -1
      val index = stackNum * size + tops(stackNum) - 1
      data(index)

    def isEmpty(stackNum: Int): Boolean = tops(stackNum) == 0
  }

  @main def main(): Unit =
    val stacks = new TripleInOne(2)
    stacks.push(0, 10)
    stacks.push(0, 11)
    stacks.push(0, 12)
    stacks.push(1, 20)
    println(stacks.peek(0))
    println(stacks.pop(0))
    println(stacks.pop(0))
    println(stacks.pop(0))
    println(stacks.isEmpty(1))
