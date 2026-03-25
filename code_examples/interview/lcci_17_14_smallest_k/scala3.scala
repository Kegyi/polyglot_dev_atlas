object Solution:
  def smallestK(arr: Array[Int], k: Int): Array[Int] =
    arr.sorted.take(k)
