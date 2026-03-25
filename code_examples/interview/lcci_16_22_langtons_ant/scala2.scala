object Lcci1622LangtonsAnt {
    private def key(r: Int, c: Int): String = s"$r#$c"

    def printKMoves(k: Int): Array[String] = {
        var r = 0
        var c = 0
        var dir = 0
        val dr = Array(0, 1, 0, -1)
        val dc = Array(1, 0, -1, 0)
        val dirs = "RDLU"

        val black = scala.collection.mutable.Set[String]()
        var minR = 0
        var maxR = 0
        var minC = 0
        var maxC = 0

        for (_ <- 0 until k) {
            val cur = key(r, c)
            if (black.contains(cur)) {
                black -= cur
                dir = (dir + 3) % 4
            } else {
                black += cur
                dir = (dir + 1) % 4
            }
            r += dr(dir)
            c += dc(dir)
            minR = math.min(minR, r)
            maxR = math.max(maxR, r)
            minC = math.min(minC, c)
            maxC = math.max(maxC, c)
        }

        black.foreach { p =>
            val parts = p.split("#")
            val br = parts(0).toInt
            val bc = parts(1).toInt
            minR = math.min(minR, br)
            maxR = math.max(maxR, br)
            minC = math.min(minC, bc)
            maxC = math.max(maxC, bc)
        }

        val board = scala.collection.mutable.ArrayBuffer[String]()
        for (i <- minR to maxR) {
            val row = new StringBuilder
            for (j <- minC to maxC) {
                if (i == r && j == c) row += dirs(dir)
                else if (black.contains(key(i, j))) row += 'X'
                else row += '_'
            }
            board += row.toString
        }
        board.toArray
    }

    def main(args: Array[String]): Unit = {
        println(printKMoves(2).mkString("[", ", ", "]"))
    }
}
