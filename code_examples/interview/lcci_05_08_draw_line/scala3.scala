object Lcci0508DrawLine:
  def drawLine(length: Int, w: Int, x1: Int, x2: Int, y: Int): Array[Int] =
    val wordsPerRow = w / 32
    val screen = new Array[Int](length)
    val offset = y * wordsPerRow
    val startWord = x1 / 32 + offset
    val endWord = x2 / 32 + offset
    val startBit = x1 % 32
    val endBit = x2 % 32

    for (i <- startWord to endWord) {
      val hi = if (i == startWord) 0xFF >> startBit else 0xFF
      val lo = if (i == endWord) ~(0xFF >> (endBit + 1)) else 0xFF
      screen(i) = hi & lo
    }
    screen

  @main def main(): Unit =
    val result = drawLine(1, 32, 1, 30, 0)
    result.foreach(v => println(v.toHexString))
