object Lcci0813PileBox {
    def pileBox(box: Array[Array[Int]]): Int = {
        val sorted = box.sortWith((a, b) => if (a(0) != b(0)) a(0) > b(0) else a(1) > b(1))
        val n = sorted.length
        val dp = sorted.map(_(2))
        var ans = dp.max
        for (i <- 1 until n) {
            for (j <- 0 until i) {
                if (sorted(j)(0) > sorted(i)(0) && sorted(j)(1) > sorted(i)(1) && sorted(j)(2) > sorted(i)(2)) {
                    if (dp(j) + sorted(i)(2) > dp(i)) dp(i) = dp(j) + sorted(i)(2)
                }
            }
            if (dp(i) > ans) ans = dp(i)
        }
        ans
    }

    def main(args: Array[String]): Unit = {
        println(pileBox(Array(Array(2,2,2), Array(3,3,3), Array(4,4,4)))) // 9
    }
}
