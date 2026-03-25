import java.nio.file.{Files, Path}
import scala.jdk.CollectionConverters.*

object FileIOBasics:
  @main def main(): Unit =
    val path = Path.of("file_io_demo.txt")
    Files.writeString(path, "apple\nbanana\ncarrot\n")

    val lines = Files.readAllLines(path).asScala.toSeq
    println(s"read lines: $lines")
