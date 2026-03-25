object Lcci1615MasterMind {
    def masterMind(solution: String, guess: String): Array[Int] = {
        var hits = 0
        val cs = Array.fill(26)(0)
        val cg = Array.fill(26)(0)
        for (i <- 0 until 4) {
            if (solution(i) == guess(i)) {
                hits += 1
            } else {
                cs(solution(i) - 'A') += 1
                cg(guess(i) - 'A') += 1
            }
        }
        var pseudo = 0
        for (i <- 0 until 26) {
            pseudo += math.min(cs(i), cg(i))
        }
        Array(hits, pseudo)
    }

    def main(args: Array[String]): Unit = {
        println(masterMind("RGBY", "GGRR").mkString("[", ", ", "]"))
    }
}
