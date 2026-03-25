object Solution:
  def massage(nums: Array[Int]): Int =
    var f = 0
    var g = 0
    for (x <- nums) {
      val nf = g + x
      val ng = f.max(g)
      f = nf
      g = ng
    }
    f.max(g)
