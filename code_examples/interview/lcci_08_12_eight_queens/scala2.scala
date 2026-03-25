object Lcci0812EightQueens {
    def solveNQueens(n: Int): Array[Array[String]] = {
        val result = scala.collection.mutable.ArrayBuffer[Array[String]]()
        val usedCols = scala.collection.mutable.Set[Int]()
        val diag1 = scala.collection.mutable.Set[Int]()
        val diag2 = scala.collection.mutable.Set[Int]()
        val board = Array.fill(n)(Array.fill(n)('.'))

        def bt(row: Int): Unit = {
            if (row == n) {
                result += board.map(_.mkString)
                return
            }
            for (col <- 0 until n) {
                if (!usedCols(col) && !diag1(row - col) && !diag2(row + col)) {
                    board(row)(col) = 'Q'
                    usedCols += col; diag1 += (row - col); diag2 += (row + col)
                    bt(row + 1)
                    board(row)(col) = '.'
                    usedCols -= col; diag1 -= (row - col); diag2 -= (row + col)
                }
            }
        }

        bt(0)
        result.toArray
    }

    def main(args: Array[String]): Unit = {
        val result = solveNQueens(4)
        println(s"${result.length} solutions")
        for (board <- result) {
            board.foreach(println)
            println()
        }
    }
}
