import scala.collection.mutable

object Solution:
  def findLadders(beginWord: String, endWord: String, wordList: Array[String]): Array[String] =
    val wordSet = wordList.toSet
    if (!wordSet.contains(endWord)) return Array()

    val queue = mutable.Queue[List[String]](List(beginWord))
    val visited = mutable.Set[String](beginWord)

    while (queue.nonEmpty) {
      val path = queue.dequeue()
      val cur = path.last
      for (i <- cur.indices) {
        for (c <- 'a' to 'z') {
          if (c != cur(i)) {
            val nxt = cur.updated(i, c)
            if (nxt == endWord) return (path :+ nxt).toArray
            if (wordSet.contains(nxt) && !visited.contains(nxt)) {
              visited.add(nxt)
              queue.enqueue(path :+ nxt)
            }
          }
        }
      }
    }
    Array()
