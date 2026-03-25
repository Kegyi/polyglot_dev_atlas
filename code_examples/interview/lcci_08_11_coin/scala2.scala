object Lcci0811Coin {
    def waysToChange(n: Int): Int = {
        val MOD = 1000000007L
        val coins = Array(1, 5, 10, 25)
        val dp = Array.fill(n + 1)(0L)
        dp(0) = 1L
        for (coin <- coins) {
            for (i <- coin to n) {
                dp(i) = (dp(i) + dp(i - coin)) % MOD
            }
        }
        dp(n).toInt
    }

    def main(args: Array[String]): Unit = {
        println(waysToChange(5))   // 2
        println(waysToChange(10))  // 4
    }
}
