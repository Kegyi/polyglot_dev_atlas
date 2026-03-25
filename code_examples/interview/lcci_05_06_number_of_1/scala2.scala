object Lcci0506NumberOf1 {
  def convertInteger(A: Int, B: Int): Int =
    Integer.bitCount(A ^ B)

  def main(args: Array[String]): Unit = {
    println(convertInteger(29, 15))
    println(convertInteger(1, 5))
  }
}
