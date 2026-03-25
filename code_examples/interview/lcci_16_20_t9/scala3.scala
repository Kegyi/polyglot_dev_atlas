object Lcci1620T9:
    private def mapDigit(ch: Char): Char = {
        if (ch <= 'c') '2'
        else if (ch <= 'f') '3'
        else if (ch <= 'i') '4'
        else if (ch <= 'l') '5'
        else if (ch <= 'o') '6'
        else if (ch <= 's') '7'
        else if (ch <= 'v') '8'
        else '9'
    }

    def getValidT9Words(num: String, words: Array[String]): Array[String] =
        words.filter { word =>
            word.length == num.length && word.indices.forall(i => mapDigit(word(i)) == num(i))
        }

    @main def main(): Unit =
        println(getValidT9Words("8733", Array("tree", "used", "true")).mkString("[", ", ", "]"))
