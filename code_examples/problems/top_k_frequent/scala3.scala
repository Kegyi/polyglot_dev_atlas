object TopKFrequent:
  def topKFrequent(nums: Vector[Int], k: Int): Vector[Int] =
    nums
      .groupBy(identity)
      .view
      .mapValues(_.length)
      .toVector
      .sortBy { case (_, count) => -count }
      .take(k)
      .map { case (value, _) => value }

  @main def main(): Unit =
    val nums = Vector(1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 5, 5)
    val k = 2
    val result = topKFrequent(nums, k)

    println("top k frequent: " + result.mkString(" "))
