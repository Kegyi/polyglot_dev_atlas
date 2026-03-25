object Lcci0814BooleanEvaluation:
    val MOD = 1000000007L

    def countEval(s: String, result: Int): Int =
        val n = s.length
        // dp(i)(j)(v) = ways s[i..j] evaluates to v
        val dp = Array.ofDim[Long](n, n, 2)
        for (i <- 0 until n by 2) dp(i)(i)(s(i) - '0') = 1L
        var size = 3
        while (size <= n) {
            var i = 0
            while (i <= n - size) {
                val j = i + size - 1
                var k = i + 1
                while (k < j) {
                    val op = s(k)
                    val lf = dp(i)(k-1)(0); val lt = dp(i)(k-1)(1)
                    val rf = dp(k+1)(j)(0); val rt = dp(k+1)(j)(1)
                    op match {
                        case '&' =>
                            dp(i)(j)(1) = (dp(i)(j)(1) + lt * rt) % MOD
                            dp(i)(j)(0) = (dp(i)(j)(0) + lf*rf + lf*rt + lt*rf) % MOD
                        case '|' =>
                            dp(i)(j)(1) = (dp(i)(j)(1) + lt*rt + lf*rt + lt*rf) % MOD
                            dp(i)(j)(0) = (dp(i)(j)(0) + lf*rf) % MOD
                        case '^' =>
                            dp(i)(j)(1) = (dp(i)(j)(1) + lf*rt + lt*rf) % MOD
                            dp(i)(j)(0) = (dp(i)(j)(0) + lf*rf + lt*rt) % MOD
                    }
                    k += 2
                }
                i += 2
            }
            size += 2
        }
        dp(0)(n-1)(result).toInt

    @main def main(): Unit =
        println(countEval("1^0|0|1", 0))      // 2
        println(countEval("0&0&0&1^1|0", 1))  // 10
