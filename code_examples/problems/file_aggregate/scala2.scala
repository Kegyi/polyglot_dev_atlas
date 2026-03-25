import scala.io.Source
import scala.concurrent.{Future, Await}
import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.duration.Duration
import scala.util.{Try, Success, Failure}

case class Record(name: String, score: Int)

object FileProcessor {
  def readAll(path: String): List[Record] = {
    val src = Source.fromFile(path)
    try {
      src.getLines().toList.flatMap { raw =>
        val line = raw.trim
        if (line.isEmpty || line.startsWith("#")) None
        else {
          line.split(",", 2).toList match {
            case name :: s :: Nil =>
              Try(s.trim.toInt) match {
                case Success(v) => Some(Record(name.trim, v))
                case Failure(_) => None
              }
            case _ => None
          }
        }
      }
    } finally {
      src.close()
    }
  }
}

object Main extends App {
  val path = if (args.nonEmpty) args(0) else "data.txt"
  try {
    val records = FileProcessor.readAll(path)
    val buckets = records.groupBy(_.name).view.mapValues(_.map(_.score)).toMap
    val futures = buckets.map { case (name, scores) =>
      Future { (name, if (scores.isEmpty) 0.0 else scores.sum.toDouble / scores.size) }
    }
    val aggregated = Future.sequence(futures.toList).map(_.sortBy(-_._2))
    val results = Await.result(aggregated, Duration.Inf)
    results.foreach { case (name, avg) => println(f"$name: $avg%.2f") }
  } catch {
    case ex: Throwable => System.err.println(s"Error: ${ex.getMessage}"); System.exit(1)
  }
}
