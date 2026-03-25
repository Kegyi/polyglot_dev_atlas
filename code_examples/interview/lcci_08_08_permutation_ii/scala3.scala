object Lcci0808PermutationIi:
    def permutation(S: String): Array[String] =
        val chars = S.toCharArray.sorted
        val result = scala.collection.mutable.ArrayBuffer[String]()
        val used = Array.fill(chars.length)(false)
        val path = scala.collection.mutable.ArrayBuffer[Char]()

        def backtrack(): Unit =
            if (path.length == chars.length) {
                result += path.mkString
                return
            }
            for (i <- chars.indices) {
                if (!used(i)) {
                    if (i > 0 && chars(i) == chars(i - 1) && !used(i - 1)) ()
                    else {
                        used(i) = true
                        path += chars(i)
                        backtrack()
                        path.remove(path.length - 1)
                        used(i) = false
                    }
                }
            }

        backtrack()
        result.toArray

    @main def main(): Unit =
        permutation("qqe").foreach(println)
