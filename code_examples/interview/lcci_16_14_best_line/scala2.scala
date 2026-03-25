object Lcci1614BestLine {
    private def collinear(a: Array[Int], b: Array[Int], c: Array[Int]): Boolean = {
        val x1 = b(0).toLong - a(0).toLong
        val y1 = b(1).toLong - a(1).toLong
        val x2 = c(0).toLong - a(0).toLong
        val y2 = c(1).toLong - a(1).toLong
        x1 * y2 == x2 * y1
    }

    def bestLine(points: Array[Array[Int]]): Array[Int] = {
        val n = points.length
        var bestI = 0
        var bestJ = 1
        var bestCount = 2
        for (i <- 0 until n) {
            for (j <- i + 1 until n) {
                var count = 2
                for (k <- j + 1 until n) {
                    if (collinear(points(i), points(j), points(k))) count += 1
                }
                if (count > bestCount || (count == bestCount && (i < bestI || (i == bestI && j < bestJ)))) {
                    bestI = i
                    bestJ = j
                    bestCount = count
                }
            }
        }
        Array(bestI, bestJ)
    }

    def main(args: Array[String]): Unit = {
        println(bestLine(Array(Array(0, 0), Array(1, 1), Array(1, 0), Array(2, 2))).mkString("[", ", ", "]"))
    }
}
