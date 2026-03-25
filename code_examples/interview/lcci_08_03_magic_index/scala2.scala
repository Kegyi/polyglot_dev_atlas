object Lcci0803MagicIndex {
    def findMagicIndex(nums: Array[Int]): Int = {
        var lo = 0; var hi = nums.length - 1
        while (lo <= hi) {
            val mid = lo + (hi - lo) / 2
            if (nums(mid) == mid) return mid
            if (nums(mid) < mid) lo = mid + 1
            else hi = mid - 1
        }
        -1
    }

    def main(args: Array[String]): Unit = {
        println(findMagicIndex(Array(-1, 1, 3, 4, 6))) // 1
        println(findMagicIndex(Array(0, 2, 3, 4, 5)))  // 0
    }
}
