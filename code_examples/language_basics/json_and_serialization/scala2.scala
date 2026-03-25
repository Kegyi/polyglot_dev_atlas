object JsonAndSerializationBasics {
  def toJson(name: String, age: Int): String = {
    s"{\"name\":\"$name\",\"age\":$age}"
  }

  def extractName(json: String): String = {
    val pattern = """\"name\":\"([^\"]+)\""".r
    pattern.findFirstMatchIn(json).map(_.group(1)).getOrElse("")
  }

  def main(args: Array[String]): Unit = {
    val json = toJson("Alice", 29)
    println(s"json: $json")
    println(s"parsed name: ${extractName(json)}")
  }
}
