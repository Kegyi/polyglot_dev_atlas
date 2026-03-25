object Lcci0103StringToUrl:
  def urlify(s: String, trueLength: Int): String =
    val b = new StringBuilder
    for (i <- 0 until trueLength) {
      if (s(i) == ' ') {
        b.append("%20")
      } else {
        b.append(s(i))
      }
    }
    b.toString()

  @main def main(): Unit =
    println(urlify("Mr John Smith    ", 13))
