object Solution:
  def shortestSeq(big: Array[Int], small: Array[Int]): Array[Int] =
    val need = scala.collection.mutable.Map[Int, Int]()
    for (x <- small) need(x) = need.getOrElse(x, 0) + 1
    val window = scala.collection.mutable.Map[Int, Int]()
    var cnt = small.length
    var j = 0; var k = -1; var mi = Int.MaxValue

    for (i <- big.indices) {
      val x = big(i)
      window(x) = window.getOrElse(x, 0) + 1
      if (need.getOrElse(x, 0) >= window(x)) cnt -= 1
      while (cnt == 0) {
        if (i - j + 1 < mi) { mi = i - j + 1; k = j }
        val lx = big(j)
        if (need.getOrElse(lx, 0) >= window.getOrElse(lx, 0)) cnt += 1
        window(lx) = window.getOrElse(lx, 0) - 1
        j += 1
      }
    }
    if (k == -1) Array() else Array(k, k + mi - 1)
