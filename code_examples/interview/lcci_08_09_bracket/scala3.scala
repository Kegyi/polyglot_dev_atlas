object Lcci0809Bracket:
    def generateParenthesis(n: Int): Array[String] =
        val result = scala.collection.mutable.ArrayBuffer[String]()

        def bt(cur: String, open: Int, close: Int): Unit =
            if (cur.length == 2 * n) { result += cur; return }
            if (open < n) bt(cur + "(", open + 1, close)
            if (close < open) bt(cur + ")", open, close + 1)

        bt("", 0, 0)
        result.toArray

    @main def main(): Unit =
        generateParenthesis(3).foreach(println)
