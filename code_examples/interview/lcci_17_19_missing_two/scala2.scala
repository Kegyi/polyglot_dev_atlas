object Solution {
  def missingTwo(nums: Array[Int]): Array[Int] = {
    val n = nums.length + 2
    var xor = 0
    for (v <- nums) xor ^= v
    for (i <- 1 to n) xor ^= i
    val diff = xor & (-xor)
    var a = 0
    for (v <- nums) if ((v & diff) != 0) a ^= v
    for (i <- 1 to n) if ((i & diff) != 0) a ^= i
    val b = xor ^ a
    Array(a, b)
  }
}
