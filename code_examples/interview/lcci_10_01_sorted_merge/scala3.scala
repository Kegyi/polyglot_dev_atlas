object Lcci1001SortedMerge:
    def merge(a: Array[Int], m: Int, b: Array[Int], n: Int): Unit =
        var i = m - 1
        var j = n - 1
        var k = m + n - 1
        while (j >= 0) {
            if (i >= 0 && a(i) > b(j)) {
                a(k) = a(i)
                i -= 1
            } else {
                a(k) = b(j)
                j -= 1
            }
            k -= 1
        }

    @main def main(): Unit =
        val a = Array(1, 2, 3, 0, 0, 0)
        merge(a, 3, Array(2, 5, 6), 3)
        println(a.mkString("[", ", ", "]"))
