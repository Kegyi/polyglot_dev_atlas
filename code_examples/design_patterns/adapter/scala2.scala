// Adapter
trait Printer {
    def printText(text: String): Unit
}

case class TextPrinter() extends Printer {
    def printText(text: String): Unit = println(s"Printing: $text")
}

class JSONObject(val data: Map[String, String])

class JSONToPrinterAdapter(json: JSONObject) extends Printer {
    def printText(text: String): Unit = {
        println(s"Adapted JSON: ${json.data.toString()}")
    }
}

object Main extends App {
    val textPrinter: Printer = TextPrinter()
    textPrinter.printText("Hello")
    
    val json = JSONObject(Map("key" -> "value"))
    val adaptedPrinter: Printer = JSONToPrinterAdapter(json)
    adaptedPrinter.printText("")
}
