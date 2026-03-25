object Lcci0302MinStack {
  final class MinStack {
    private val values = scala.collection.mutable.ArrayBuffer.empty[Int]
    private val mins = scala.collection.mutable.ArrayBuffer.empty[Int]

    def push(x: Int): Unit = {
      values += x
      if (mins.isEmpty || x <= mins.last) mins += x
    }

    def pop(): Unit = {
      if (values.isEmpty) return
      val top = values.remove(values.length - 1)
      if (top == mins.last) mins.remove(mins.length - 1)
    }

    def top(): Int = if (values.isEmpty) -1 else values.last

    def getMin(): Int = if (mins.isEmpty) -1 else mins.last
  }

  def main(args: Array[String]): Unit = {
    val st = new MinStack
    st.push(3)
    st.push(5)
    st.push(2)
    st.push(2)
    println(st.getMin())
    st.pop()
    println(st.getMin())
    st.pop()
    println(st.getMin())
  }
}
