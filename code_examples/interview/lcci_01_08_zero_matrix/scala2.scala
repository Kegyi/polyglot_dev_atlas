object Lcci0108ZeroMatrix {
  def setZeroes(matrix: Array[Array[Int]]): Unit = {
    val zeroRows = scala.collection.mutable.Set.empty[Int]
    val zeroCols = scala.collection.mutable.Set.empty[Int]

    for (r <- matrix.indices; c <- matrix(0).indices) {
      if (matrix(r)(c) == 0) {
        zeroRows += r
        zeroCols += c
      }
    }

    for (r <- matrix.indices; c <- matrix(0).indices) {
      if (zeroRows.contains(r) || zeroCols.contains(c)) {
        matrix(r)(c) = 0
      }
    }
  }

  def main(args: Array[String]): Unit = {
    val matrix = Array(
      Array(1, 2, 3),
      Array(4, 0, 6),
      Array(7, 8, 9)
    )

    setZeroes(matrix)
    matrix.foreach(row => println(row.mkString(" ")))
  }
}
