object CommandLineArgsBasics {
  def main(args: Array[String]): Unit = {
    val name = if (args.nonEmpty) args(0) else "world"
    val excited = args.contains("--excited")

    val suffix = if (excited) "!" else ""
    println(s"Hello, $name$suffix")
  }
}
