import java.nio.file.{Files, Path}
import scala.jdk.CollectionConverters._

object FileIOBasics {
  def main(args: Array[String]): Unit = {
    val path = Path.of("file_io_demo.txt")
    Files.writeString(path, "apple\nbanana\ncarrot\n")

    val lines = Files.readAllLines(path).asScala.toSeq
    println(s"read lines: $lines")
  }
}
