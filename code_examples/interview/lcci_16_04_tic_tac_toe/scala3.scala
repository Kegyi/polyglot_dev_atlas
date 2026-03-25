object Lcci1604TicTacToe:
    def tictactoe(board: Array[String]): String =
        val n = board.length

        def winner(c: Char): Boolean =
            for (i <- 0 until n) {
                var row = true
                var col = true
                for (j <- 0 until n) {
                    row = row && board(i)(j) == c
                    col = col && board(j)(i) == c
                }
                if (row || col) return true
            }
            var diag1 = true
            var diag2 = true
            for (i <- 0 until n) {
                diag1 = diag1 && board(i)(i) == c
                diag2 = diag2 && board(i)(n - 1 - i) == c
            }
            diag1 || diag2

        if (winner('X')) return "X"
        if (winner('O')) return "O"
        if (board.exists(_.contains(' '))) return "Pending"
        "Draw"

    @main def main(): Unit =
        println(tictactoe(Array("O X", " XO", "X O")))
        println(tictactoe(Array("OOX", "XXO", "OXO")))
