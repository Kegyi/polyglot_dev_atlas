import java.nio.file.{Files, Paths}

object FilePathsAndDirectoriesBasics {
  def main(args: Array[String]): Unit = {
    val filePath = Paths.get("demo_folder", "sub", "data.txt")
    val parent = filePath.getParent

    Files.createDirectories(parent)

    println(s"file path: $filePath")
    println(s"parent path: $parent")
    println(s"directory exists: ${Files.exists(parent)}")
  }
}
