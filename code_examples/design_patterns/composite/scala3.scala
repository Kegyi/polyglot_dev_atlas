// Composite
trait FileSystemNode:
    def getSize(): Long

case class File(name: String, size: Long) extends FileSystemNode:
    def getSize(): Long = size

class Folder(name: String) extends FileSystemNode:
    private var children: List[FileSystemNode] = List()
    
    def add(node: FileSystemNode): Unit =
        children = children :+ node
    
    def getSize(): Long = children.map(_.getSize()).sum

@main def main(): Unit =
    val file1 = File("file1.txt", 100)
    val file2 = File("file2.txt", 200)
    
    val folder = new Folder("documents")
    folder.add(file1)
    folder.add(file2)
    
    println(s"Folder size: ${folder.getSize()}")
