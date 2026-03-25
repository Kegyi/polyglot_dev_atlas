object Lcci1607Maximum:
    def maximum(a: Int, b: Int): Int = if (a > b) a else b

    @main def main(): Unit =
        println(maximum(1, 2))
