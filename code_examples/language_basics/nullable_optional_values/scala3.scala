object NullableOptionalValuesBasics:
  def parseAge(text: String): Option[Int] =
    if (text.isEmpty) None else Some(text.toInt)

  @main def main(): Unit =
    val age = parseAge("29")
    val missing = parseAge("")

    println(s"age present: ${age.isDefined}")
    println(s"missing default: ${missing.getOrElse(0)}")
