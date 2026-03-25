object Lcci1002GroupAnagrams:
    def groupAnagrams(strs: Array[String]): Array[Array[String]] =
        val groups = strs.groupBy(word => word.sorted).values.map(_.sorted).toArray
        groups.sortBy(_(0))

    @main def main(): Unit =
        val result = groupAnagrams(Array("eat", "tea", "tan", "ate", "nat", "bat"))
        println(result.map(_.mkString("[", ", ", "]")).mkString("[", ", ", "]"))
