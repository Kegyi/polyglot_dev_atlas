object Lcci1621SumSwap {
    def findSwapValues(array1: Array[Int], array2: Array[Int]): Array[Int] = {
        val diff = array1.sum - array2.sum
        if (diff % 2 != 0) return Array.emptyIntArray
        val target = diff / 2
        val set2 = array2.toSet
        array1.foreach { x =>
            val y = x - target
            if (set2.contains(y)) return Array(x, y)
        }
        Array.emptyIntArray
    }

    def main(args: Array[String]): Unit = {
        println(findSwapValues(Array(4, 1, 2, 1, 1, 2), Array(3, 6, 3, 3)).mkString("[", ", ", "]"))
    }
}
