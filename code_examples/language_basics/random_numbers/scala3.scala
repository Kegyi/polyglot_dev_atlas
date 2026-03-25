import scala.util.Random

object RandomNumbersBasics:
  @main def main(): Unit =
    val generator = new Random(42)
    val draws = Seq.fill(3)(generator.between(1, 11))
    println(s"draws: $draws")
