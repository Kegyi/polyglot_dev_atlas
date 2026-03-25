object Lcci1624PairsWithSum:
    def pairSums(nums: Array[Int], target: Int): Array[Array[Int]] =
        val freq = scala.collection.mutable.Map[Int, Int]().withDefaultValue(0)
        val ans = scala.collection.mutable.ArrayBuffer[Array[Int]]()
        nums.foreach { x =>
            val y = target - x
            if (freq(y) > 0) {
                freq(y) = freq(y) - 1
                ans += Array(math.min(x, y), math.max(x, y))
            } else {
                freq(x) = freq(x) + 1
            }
        }
        ans.toArray

    @main def main(): Unit =
        println(pairSums(Array(5, 6, 5), 11).map(_.mkString("[", ", ", "]")).mkString("[", ", ", "]"))
