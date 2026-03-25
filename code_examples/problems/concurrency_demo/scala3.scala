import scala.concurrent.{Future, Await}
import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.duration.Duration

object ConcurrencyDemo:
  @main def main(): Unit =
  val n = 1000
  val data = (1 to n).toArray
  val threads = Runtime.getRuntime.availableProcessors()
  val block = n / threads
  val futures = (0 until threads).map { i =>
    Future {
      val s = i * block
      val e = if (i == threads - 1) n else (i + 1) * block
      (s until e).map(j => data(j)).sum
    }
  }
  val results = Await.result(Future.sequence(futures), Duration.Inf)
  println("Total: " + results.sum)
