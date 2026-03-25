object Lcci1005SparseArraySearch:
    def findString(words: Array[String], target: String): Int =
        var left = 0
        var right = words.length - 1
        var answer = -1
        while (left <= right) {
            val mid = (left + right) / 2
            var lo = mid
            var hi = mid
            var actual = -1
            while (actual == -1 && (lo >= left || hi <= right)) {
                if (lo >= left && words(lo).nonEmpty) actual = lo
                else if (hi <= right && words(hi).nonEmpty) actual = hi
                lo -= 1
                hi += 1
            }
            if (actual == -1) {
                return answer
            }
            if (words(actual) == target) {
                answer = actual
                right = actual - 1
            } else if (words(actual) < target) {
                left = actual + 1
            } else {
                right = actual - 1
            }
        }
        answer

    @main def main(): Unit =
        val words = Array("at", "", "", "", "ball", "", "", "car", "", "", "dad", "", "")
        println(findString(words, "ta"))
        println(findString(words, "ball"))
