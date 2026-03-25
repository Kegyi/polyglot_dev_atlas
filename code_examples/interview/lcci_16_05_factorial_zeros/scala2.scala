object Lcci1605FactorialZeros {
    def trailingZeroes(n0: Int): Int = {
        var n = n0
        var ans = 0
        while (n > 0) {
            n /= 5
            ans += n
        }
        ans
    }

    def main(args: Array[String]): Unit = {
        println(trailingZeroes(3))
        println(trailingZeroes(5))
    }
}
