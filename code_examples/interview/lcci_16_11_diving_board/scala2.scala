object Lcci1611DivingBoard {
    def divingBoard(shorter: Int, longer: Int, k: Int): Array[Int] = {
        if (k == 0) return Array.emptyIntArray
        if (shorter == longer) return Array(shorter * k)
        Array.tabulate(k + 1)(i => shorter * (k - i) + longer * i)
    }

    def main(args: Array[String]): Unit = {
        println(divingBoard(1, 2, 3).mkString("[", ", ", "]"))
    }
}
