object Lcci1704MissingNumber:
  def missingNumber(nums: Array[Int]): Int =
    var ans = 0
    for (i <- 1 to nums.length) ans ^= i
    for (x <- nums) ans ^= x
    ans

  @main def main(): Unit =
    println(missingNumber(Array(3, 0, 1)))                   // 2
    println(missingNumber(Array(9, 6, 4, 2, 3, 5, 7, 0, 1))) // 8
