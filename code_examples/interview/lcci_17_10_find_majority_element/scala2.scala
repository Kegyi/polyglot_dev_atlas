object Lcci1710FindMajorityElement {
  def majorityElement(nums: Array[Int]): Int = {
    var candidate = 0
    var count = 0
    for (x <- nums) {
      if (count == 0) candidate = x
      count += (if (x == candidate) 1 else -1)
    }
    if (nums.count(_ == candidate) > nums.length / 2) candidate else -1
  }

  def main(args: Array[String]): Unit = {
    println(majorityElement(Array(1, 2, 5, 9, 5, 9, 5, 5, 5))) // 5
    println(majorityElement(Array(3, 2))) // -1
  }
}
