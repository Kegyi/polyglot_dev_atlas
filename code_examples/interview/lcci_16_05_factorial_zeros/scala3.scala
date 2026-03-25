object Lcci1605FactorialZeros:
    def trailingZeroes(n0: Int): Int =
        var n = n0
        var ans = 0
        while (n > 0) {
            n /= 5
            ans += n
        }
        ans

    @main def main(): Unit =
        println(trailingZeroes(3))
        println(trailingZeroes(5))
