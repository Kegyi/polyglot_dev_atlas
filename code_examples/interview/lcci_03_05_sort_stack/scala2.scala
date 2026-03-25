object Lcci0305SortStack {
  def sortStack(st: scala.collection.mutable.ArrayBuffer[Int]): Unit = {
    val tmp = scala.collection.mutable.ArrayBuffer.empty[Int]
    while (st.nonEmpty) {
      val cur = st.remove(st.length - 1)
      while (tmp.nonEmpty && tmp.last > cur) {
        st += tmp.remove(tmp.length - 1)
      }
      tmp += cur
    }
    while (tmp.nonEmpty) {
      st += tmp.remove(tmp.length - 1)
    }
  }

  def main(args: Array[String]): Unit = {
    val st = scala.collection.mutable.ArrayBuffer(3, 1, 4, 2)
    sortStack(st)
    println(st.reverse.mkString(" "))
  }
}
