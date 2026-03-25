object Status extends Enumeration:
  type Status = Value
  val Pending, Running, Done = Value

object EnumsAndConstantsBasics:
  val MaxRetries = 3

  @main def main(): Unit =
    val status = Status.Running
    println(s"status: ${status.toString.toLowerCase}")
    println(s"max retries: $MaxRetries")
