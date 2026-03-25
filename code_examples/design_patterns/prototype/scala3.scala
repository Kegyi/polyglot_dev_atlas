// Prototype
trait Prototype:
    def clone(): Prototype

case class Document(title: String, content: String) extends Prototype:
    def clone(): Document = this.copy()

@main def main(): Unit =
    val original = Document("Report", "Initial content")
    val copy1 = original.clone()
    val copy2 = original.clone()
    
    println(original)
    println(copy1)
    println(copy2)
