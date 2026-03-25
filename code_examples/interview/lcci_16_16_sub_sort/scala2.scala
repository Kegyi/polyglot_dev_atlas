object Lcci1616SubSort {
    def subSort(array: Array[Int]): Array[Int] = {
        val n = array.length
        var left = -1
        var right = -1

        var maxSeen = Int.MinValue
        for (i <- 0 until n) {
            if (array(i) < maxSeen) right = i else maxSeen = array(i)
        }

        var minSeen = Int.MaxValue
        for (i <- (0 until n).reverse) {
            if (array(i) > minSeen) left = i else minSeen = array(i)
        }

        if (left == -1) Array(-1, -1) else Array(left, right)
    }

    def main(args: Array[String]): Unit = {
        println(subSort(Array(1, 2, 4, 7, 10, 11, 7, 12, 7, 7, 16, 18, 19)).mkString("[", ", ", "]"))
    }
}
