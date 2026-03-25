object Lcci0107RotateMatrix:
  def rotate(matrix: Array[Array[Int]]): Unit =
    val n = matrix.length
    for (layer <- 0 until n / 2) {
      val first = layer
      val last = n - 1 - layer
      for (i <- first until last) {
        val offset = i - first
        val top = matrix(first)(i)
        matrix(first)(i) = matrix(last - offset)(first)
        matrix(last - offset)(first) = matrix(last)(last - offset)
        matrix(last)(last - offset) = matrix(i)(last)
        matrix(i)(last) = top
      }
    }

  @main def main(): Unit =
    val matrix = Array(
      Array(1, 2, 3),
      Array(4, 5, 6),
      Array(7, 8, 9)
    )

    rotate(matrix)
    matrix.foreach(row => println(row.mkString(" ")))
