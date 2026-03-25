import scala.util.Try

object ExceptionsAndRecoveryBasics {
  def parsePort(value: String): Int = value.toInt

  def main(args: Array[String]): Unit = {
    val result = Try(parsePort("not-a-number"))

    result.fold(
      error => {
        println(s"parse failed: ${error.getMessage}")
        println("fallback port: 8080")
      },
      port => println(s"port: $port")
    )

    println("program continues")
  }
}
