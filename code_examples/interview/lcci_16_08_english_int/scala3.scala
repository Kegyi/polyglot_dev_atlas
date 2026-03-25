object Lcci1608EnglishInt:
    private val ones = Array("", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine")
    private val teens = Array("Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen")
    private val tens = Array("", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety")
    private val units = Array("", "Thousand", "Million", "Billion")

    private def below1000(n0: Int): String = {
        var n = n0
        val parts = scala.collection.mutable.ArrayBuffer[String]()
        if (n >= 100) {
            parts += ones(n / 100)
            parts += "Hundred"
            n %= 100
        }
        if (n >= 20) {
            parts += tens(n / 10)
            if (n % 10 != 0) parts += ones(n % 10)
        } else if (n >= 10) {
            parts += teens(n - 10)
        } else if (n > 0) {
            parts += ones(n)
        }
        parts.mkString(" ")
    }

    def numberToWords(num0: Int): String =
        if (num0 == 0) return "Zero"
        if (num0 < 0) return "Negative " + numberToWords(-num0)

        var num = num0
        val parts = scala.collection.mutable.ArrayBuffer[String]()
        var unit = 0
        while (num > 0) {
            val chunk = num % 1000
            if (chunk > 0) {
                var piece = below1000(chunk)
                if (units(unit).nonEmpty) piece += " " + units(unit)
                parts += piece
            }
            num /= 1000
            unit += 1
        }
        parts.reverse.mkString(" ")

    @main def main(): Unit =
        println(numberToWords(123))
        println(numberToWords(12345))
        println(numberToWords(-1000010))
