object Lcci1609Operations {
    final class Operations {
        def minus(a: Int, b: Int): Int = a - b
        def multiply(a: Int, b: Int): Int = a * b
        def divide(a: Int, b: Int): Int = a / b
    }

    def main(args: Array[String]): Unit = {
        val ops = new Operations
        println(ops.minus(10, 3))
        println(ops.multiply(6, -4))
        println(ops.divide(20, 5))
    }
}
