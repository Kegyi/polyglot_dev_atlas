object MatrixMul {
  def main(args: Array[String]): Unit = {
    val N = 200
    val A = Array.tabulate(N, N)((i, j) => i + j)
    val B = Array.tabulate(N, N)((i, j) => i - j)
    val C = Array.ofDim[Int](N, N)
    for (i <- 0 until N)
      for (k <- 0 until N)
        for (j <- 0 until N)
          C(i)(j) += A(i)(k) * B(k)(j)
    println(C(0)(0))
  }
}
