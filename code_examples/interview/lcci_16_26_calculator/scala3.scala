object Lcci1626Calculator:
    def calculate(s: String): Int =
        val st = scala.collection.mutable.ArrayBuffer[Int]()
        var num = 0
        var op = '+'
        val str = s + "+"
        str.foreach { ch =>
            if (ch != ' ') {
                if (ch.isDigit) {
                    num = num * 10 + (ch - '0')
                } else {
                    op match {
                        case '+' => st += num
                        case '-' => st += -num
                        case '*' => st(st.length - 1) = st.last * num
                        case '/' => st(st.length - 1) = st.last / num
                    }
                    op = ch
                    num = 0
                }
            }
        }
        st.sum

    @main def main(): Unit =
        println(calculate("3+2*2"))
        println(calculate(" 3/2 "))
        println(calculate(" 3+5 / 2 "))
