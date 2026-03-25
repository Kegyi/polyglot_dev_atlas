object ArraysAndCollectionsBasics:
  @main def main(): Unit =
    val values = Vector(1, 2, 3, 4, 5)
    println(s"original: $values")

    val doubled = values.map(_ * 2)
    val evens = doubled.filter(_ % 2 == 0)
    val total = evens.sum

    println(s"doubled: $doubled")
    println(s"evens: $evens")
    println(s"sum of evens in doubled: $total")
