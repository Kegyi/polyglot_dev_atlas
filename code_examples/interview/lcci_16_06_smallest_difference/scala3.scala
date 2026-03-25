object Lcci1606SmallestDifference:
    def smallestDifference(a: Array[Int], b: Array[Int]): Int =
        val x = a.sorted
        val y = b.sorted
        var i = 0
        var j = 0
        var ans = Long.MaxValue
        while (i < x.length && j < y.length) {
            ans = math.min(ans, math.abs(x(i).toLong - y(j).toLong))
            if (x(i) < y(j)) i += 1 else j += 1
        }
        ans.toInt

    @main def main(): Unit =
        println(smallestDifference(Array(1, 3, 15, 11, 2), Array(23, 127, 235, 19, 8)))
