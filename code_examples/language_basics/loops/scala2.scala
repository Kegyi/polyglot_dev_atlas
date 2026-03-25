object LoopsBasics {
  def main(args: Array[String]): Unit = {
    val values = Vector(1, 2, 3, 4, 5)

    for (i <- values.indices) {
      println(s"for index: $i -> ${values(i)}")
    }

    for (v <- values) {
      if (v != 3) println(s"for each: $v")
    }

    var i = 0
    while (i < values.length && values(i) != 4) {
      println(s"while: ${values(i)}")
      i += 1
    }

    var c = 0
    do {
      println(s"do-while iteration: $c")
      c += 1
    } while (c < 2)
  }
}
