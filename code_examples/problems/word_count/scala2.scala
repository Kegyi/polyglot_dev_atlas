import scala.io.Source

object WordCount {
  def main(args: Array[String]): Unit = {
    val path = if (args.nonEmpty) args(0) else "data.txt"

    val source = Source.fromFile(path)
    val text = try source.mkString.toLowerCase finally source.close()

    val words = "\\w+".r.findAllIn(text).toList
    val counts = words.groupBy(identity).view.mapValues(_.size).toSeq.sortBy(-_._2)
    counts.foreach { case (w, c) => println(s"$w: $c") }
  }
}
