object EnvironmentVariablesBasics {
  def main(args: Array[String]): Unit = {
    val env = sys.env
    val mode = env.getOrElse("APP_MODE", "development")
    val port = env.getOrElse("APP_PORT", "8080")

    println(s"mode: $mode")
    println(s"port: $port")
    println(s"has APP_MODE: ${env.contains("APP_MODE")}")
  }
}
