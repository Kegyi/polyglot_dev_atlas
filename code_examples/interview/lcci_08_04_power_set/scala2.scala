object Lcci0804PowerSet {
    def subsets(nums: Array[Int]): Array[Array[Int]] = {
        val sorted = nums.sorted
        val n = sorted.length
        (0 until (1 << n)).map { mask =>
            (0 until n).filter(i => (mask & (1 << i)) != 0).map(sorted(_)).toArray
        }.toArray
    }

    def main(args: Array[String]): Unit = {
        for (s <- subsets(Array(1, 2, 3))) {
            println(s.mkString("[", ",", "]"))
        }
    }
}
