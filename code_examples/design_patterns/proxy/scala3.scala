// Proxy
trait Image:
    def display(): Unit

class RealImage(filename: String) extends Image:
    private def loadFromDisk(): Unit = println(s"Loading $filename from disk")
    
    def display(): Unit =
        loadFromDisk()
        println(s"Displaying $filename")

class ImageProxy(filename: String) extends Image:
    private var realImage: Option[RealImage] = None
    
    def display(): Unit =
        if (realImage.isEmpty) {
            realImage = Some(new RealImage(filename))
        }
        realImage.get.display()

@main def main(): Unit =
    val image: Image = new ImageProxy("photo.jpg")
    image.display()
    image.display()
