object Lcci1618PatternMatching:
    def patternMatching(pattern: String, value: String): Boolean =
        if (pattern.isEmpty) return value.isEmpty

        var countA = 0
        var countB = 0
        pattern.foreach(ch => if (ch == 'a') countA += 1 else countB += 1)

        if (countA < countB) {
            val swapped = pattern.map(ch => if (ch == 'a') 'b' else 'a')
            return patternMatching(swapped, value)
        }

        if (value.isEmpty) return countB == 0

        val n = value.length
        var lenA = 0
        while (countA * lenA <= n) {
            val rest = n - countA * lenA
            var lenB = 0
            var valid = true
            if (countB == 0) {
                if (rest != 0) valid = false
            } else {
                if (rest % countB != 0) valid = false
                else lenB = rest / countB
            }

            if (valid) {
                var pos = 0
                var a: String = null
                var b: String = null
                var ok = true
                pattern.foreach { ch =>
                    if (ok && ch == 'a') {
                        val sub = value.substring(pos, pos + lenA)
                        if (a == null) a = sub
                        else if (a != sub) ok = false
                        pos += lenA
                    } else if (ok) {
                        val sub = value.substring(pos, pos + lenB)
                        if (b == null) b = sub
                        else if (b != sub) ok = false
                        pos += lenB
                    }
                }
                if (ok && a != b) return true
            }
            lenA += 1
        }
        false

    @main def main(): Unit =
        println(patternMatching("abba", "dogcatcatdog"))
        println(patternMatching("abba", "dogcatcatfish"))
