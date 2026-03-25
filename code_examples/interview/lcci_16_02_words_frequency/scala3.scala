object Lcci1602WordsFrequency:
    final class WordsFrequency(book: Array[String]) {
        private val counter = scala.collection.mutable.Map[String, Int]().withDefaultValue(0)
        book.foreach(word => counter(word) = counter(word) + 1)

        def get(word: String): Int = counter(word)
    }

    @main def main(): Unit =
        val wf = new WordsFrequency(Array("i", "have", "an", "apple", "he", "have", "a", "pen"))
        println(wf.get("have"))
        println(wf.get("you"))
