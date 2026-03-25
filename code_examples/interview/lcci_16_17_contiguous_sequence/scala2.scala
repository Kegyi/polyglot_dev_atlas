object Lcci1617ContiguousSequence {
    def maxSubArray(nums: Array[Int]): Int = {
        var best = nums(0)
        var cur = nums(0)
        for (i <- 1 until nums.length) {
            cur = math.max(nums(i), cur + nums(i))
            best = math.max(best, cur)
        }
        best
    }

    def main(args: Array[String]): Unit = {
        println(maxSubArray(Array(-2, 1, -3, 4, -1, 2, 1, -5, 4)))
    }
}
