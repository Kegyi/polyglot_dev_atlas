object Lcci1601SwapNumbers:
    def swapNumbers(numbers: Array[Int]): Array[Int] = Array(numbers(1), numbers(0))

    @main def main(): Unit =
        println(swapNumbers(Array(1, 2)).mkString("[", ", ", "]"))
