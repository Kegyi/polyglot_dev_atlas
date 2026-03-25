object MapsAndSetsBasics {
  def main(args: Array[String]): Unit = {
    val counts = scala.collection.mutable.Map("apple" -> 2, "banana" -> 1)
    counts("apple") = counts("apple") + 3

    val tags = scala.collection.mutable.Set("fruit", "food")
    tags += "fresh"

    println(s"apple count: ${counts("apple")}")
    println(s"all map entries: ${counts.toSeq.sortBy(_._1)}")
    println(s"all set entries: ${tags.toSeq.sorted}")
  }
}
