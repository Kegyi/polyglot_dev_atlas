object Lcci1601SwapNumbers {
    def swapNumbers(numbers: Array[Int]): Array[Int] = Array(numbers(1), numbers(0))

    def main(args: Array[String]): Unit = {
        println(swapNumbers(Array(1, 2)).mkString("[", ", ", "]"))
    }
}
