object Lcci1619PondSizes {
    def pondSizes(land: Array[Array[Int]]): Array[Int] = {
        val m = land.length
        val n = land(0).length

        def dfs(r: Int, c: Int): Int = {
            if (r < 0 || r >= m || c < 0 || c >= n || land(r)(c) != 0) return 0
            land(r)(c) = -1
            var size = 1
            for (dr <- -1 to 1) {
                for (dc <- -1 to 1) {
                    if (dr != 0 || dc != 0) size += dfs(r + dr, c + dc)
                }
            }
            size
        }

        val ans = scala.collection.mutable.ArrayBuffer[Int]()
        for (i <- 0 until m; j <- 0 until n) {
            if (land(i)(j) == 0) ans += dfs(i, j)
        }
        ans.sorted.toArray
    }

    def main(args: Array[String]): Unit = {
        val land = Array(Array(0, 2, 1, 0), Array(0, 1, 0, 1), Array(1, 1, 0, 1), Array(0, 1, 0, 1))
        println(pondSizes(land).mkString("[", ", ", "]"))
    }
}
