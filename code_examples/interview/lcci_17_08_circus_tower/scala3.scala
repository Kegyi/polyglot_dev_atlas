object Lcci1708CircusTower:
  def bestSeqAtIndex(height: Array[Int], weight: Array[Int]): Int =
    val people = height.indices.map(i => (height(i), weight(i))).sortBy(x => (x._1, -x._2))
    val lis = scala.collection.mutable.ArrayBuffer[Int]()

    for ((_, w) <- people) {
      var l = 0
      var r = lis.length
      while (l < r) {
        val m = (l + r) / 2
        if (lis(m) < w) l = m + 1
        else r = m
      }
      if (l == lis.length) lis += w
      else lis(l) = w
    }
    lis.length

  @main def main(): Unit =
    println(bestSeqAtIndex(Array(65, 70, 56, 75, 60, 68), Array(100, 150, 90, 190, 95, 110))) // 6
    println(bestSeqAtIndex(Array(65, 70, 56, 75), Array(100, 150, 90, 190))) // 4
