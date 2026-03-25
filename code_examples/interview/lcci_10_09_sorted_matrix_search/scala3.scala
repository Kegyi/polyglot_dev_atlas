object Lcci1009SortedMatrixSearch:
    def searchMatrix(matrix: Array[Array[Int]], target: Int): Boolean =
        if (matrix.isEmpty || matrix(0).isEmpty) {
            return false
        }
        var row = 0
        var col = matrix(0).length - 1
        while (row < matrix.length && col >= 0) {
            if (matrix(row)(col) == target) return true
            if (matrix(row)(col) > target) col -= 1 else row += 1
        }
        false

    @main def main(): Unit =
        val matrix = Array(
            Array(1, 4, 7, 11, 15),
            Array(2, 5, 8, 12, 19),
            Array(3, 6, 9, 16, 22),
            Array(10, 13, 14, 17, 24),
            Array(18, 21, 23, 26, 30)
        )
        println(searchMatrix(matrix, 5))
        println(searchMatrix(matrix, 20))
