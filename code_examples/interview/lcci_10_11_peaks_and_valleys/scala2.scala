object Lcci1011PeaksAndValleys {
    def wiggleSort(nums: Array[Int]): Unit = {
        scala.util.Sorting.quickSort(nums)
        var index = 0
        while (index + 1 < nums.length) {
            val tmp = nums(index)
            nums(index) = nums(index + 1)
            nums(index + 1) = tmp
            index += 2
        }
    }

    def main(args: Array[String]): Unit = {
        val nums = Array(5, 3, 1, 2, 3)
        wiggleSort(nums)
        println(nums.mkString("[", ", ", "]"))
    }
}
