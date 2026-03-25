object Lcci1707BabyNames {
  def trulyMostPopular(names: Array[String], synonyms: Array[String]): Array[String] = {
    val parent = scala.collection.mutable.Map[String, String]()

    def find(x: String): String = {
      if (!parent.contains(x)) parent(x) = x
      if (parent(x) != x) parent(x) = find(parent(x))
      parent(x)
    }

    def unite(a: String, b: String): Unit = {
      val pa = find(a)
      val pb = find(b)
      if (pa != pb) {
        if (pa < pb) parent(pb) = pa
        else parent(pa) = pb
      }
    }

    val freq = scala.collection.mutable.Map[String, Int]()
    for (s <- names) {
      val idx = s.indexOf('(')
      val name = s.substring(0, idx)
      val count = s.substring(idx + 1, s.length - 1).toInt
      freq(name) = count
    }

    for (syn <- synonyms) {
      val s = syn.substring(1, syn.length - 1)
      val comma = s.indexOf(',')
      unite(s.substring(0, comma), s.substring(comma + 1))
    }

    val result = scala.collection.mutable.Map[String, Int]().withDefaultValue(0)
    for ((name, cnt) <- freq) result(find(name)) += cnt

    result.toArray.sortBy(_._1).map { case (name, cnt) => s"$name($cnt)" }
  }

  def main(args: Array[String]): Unit = {
    val names = Array("John(15)", "Jon(12)", "Chris(13)", "Kris(4)", "Christopher(19)")
    val synonyms = Array("(Jon,John)", "(John,Johnny)", "(Chris,Kris)", "(Chris,Christopher)")
    println(trulyMostPopular(names, synonyms).mkString(" ")) // Chris(36) John(27)
  }
}
