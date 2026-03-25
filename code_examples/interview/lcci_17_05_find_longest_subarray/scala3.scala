object Lcci1705FindLongestSubarray:
  def findLongestSubarray(array: Array[String]): Array[String] =
    val first = scala.collection.mutable.Map(0 -> -1)
    var s = 0
    var maxLen = 0
    var start = 0
    for (i <- array.indices) {
      s += (if (array(i)(0).isLetter) 1 else -1)
      if (first.contains(s)) {
        val length = i - first(s)
        if (length > maxLen) {
          maxLen = length
          start = first(s) + 1
        }
      } else {
        first(s) = i
      }
    }
    array.slice(start, start + maxLen)

  @main def main(): Unit =
    val arr1 = Array("A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M")
    println(findLongestSubarray(arr1).mkString(" ")) // A 1 B C D 2 3 4 E 5 F G 6 7

    val arr2 = Array("A", "A")
    val res2 = findLongestSubarray(arr2)
    println(if (res2.isEmpty) "(empty)" else res2.mkString(" "))
