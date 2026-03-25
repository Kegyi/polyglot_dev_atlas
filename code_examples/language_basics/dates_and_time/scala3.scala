import java.time.LocalDateTime

object DatesAndTimeBasics:
  @main def main(): Unit =
    val now = LocalDateTime.now()
    val later = now.plusMinutes(90)

    println(s"now: $now")
    println(s"later: $later")
    println(s"later > now: ${later.isAfter(now)}")
