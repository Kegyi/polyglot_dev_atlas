object Lcci0801ThreeSteps:
    def waysToStep(n: Int): Int =
        val MOD = 1000000007L
        if (n == 1) return 1
        if (n == 2) return 2
        if (n == 3) return 4
        var a = 1L; var b = 2L; var c = 4L
        for (_ <- 3 until n) {
            val d = ((a + b) % MOD + c) % MOD
            a = b; b = c; c = d
        }
        c.toInt

    @main def main(): Unit =
        println(waysToStep(3)) // 4
        println(waysToStep(5)) // 13
