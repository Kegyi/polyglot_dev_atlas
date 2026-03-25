object SortingAndSearchingBasics:
  @main def main(): Unit =
    val values = Vector(9, 3, 7, 1, 5).sorted
    val index = values.indexOf(7)

    println(s"sorted: $values")
    println(s"contains 7: ${index >= 0}")
    println(s"index of 7: $index")
