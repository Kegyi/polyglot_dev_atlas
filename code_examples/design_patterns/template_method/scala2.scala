// Template Method
abstract class DataProcessor {
    final def process(): Unit = {
        readData()
        parseData()
        writeData()
    }
    
    protected def readData(): Unit
    protected def parseData(): Unit
    protected def writeData(): Unit
}

class CSVProcessor extends DataProcessor {
    protected def readData(): Unit = println("Reading CSV data")
    protected def parseData(): Unit = println("Parsing CSV")
    protected def writeData(): Unit = println("Writing processed CSV")
}

class JSONProcessor extends DataProcessor {
    protected def readData(): Unit = println("Reading JSON data")
    protected def parseData(): Unit = println("Parsing JSON")
    protected def writeData(): Unit = println("Writing processed JSON")
}

object Main extends App {
    val csv: DataProcessor = new CSVProcessor()
    csv.process()
    
    println()
    
    val json: DataProcessor = new JSONProcessor()
    json.process()
}
