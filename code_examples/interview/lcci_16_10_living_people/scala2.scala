object Lcci1610LivingPeople {
    def maxAliveYear(birth: Array[Int], death: Array[Int]): Int = {
        val diff = Array.fill(102)(0)
        for (i <- birth.indices) {
            diff(birth(i) - 1900) += 1
            if (death(i) + 1 <= 2000) {
                diff(death(i) + 1 - 1900) -= 1
            }
        }

        var bestYear = 1900
        var alive = 0
        var bestAlive = -1
        for (i <- 0 to 100) {
            alive += diff(i)
            if (alive > bestAlive) {
                bestAlive = alive
                bestYear = 1900 + i
            }
        }
        bestYear
    }

    def main(args: Array[String]): Unit = {
        println(maxAliveYear(Array(1900, 1901, 1950), Array(1948, 1951, 2000)))
    }
}
