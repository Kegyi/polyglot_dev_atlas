object Lcci1625LruCache {
    final class LRUCache(capacity: Int) {
        private val data = scala.collection.mutable.LinkedHashMap[Int, Int]()

        def get(key: Int): Int = {
            data.get(key) match {
                case None => -1
                case Some(v) =>
                    data -= key
                    data += (key -> v)
                    v
            }
        }

        def put(key: Int, value: Int): Unit = {
            if (data.contains(key)) data -= key
            data += (key -> value)
            if (data.size > capacity) {
                val oldest = data.head._1
                data -= oldest
            }
        }
    }

    def main(args: Array[String]): Unit = {
        val cache = new LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        println(cache.get(1))
        cache.put(3, 3)
        println(cache.get(2))
        cache.put(4, 4)
        println(cache.get(1))
        println(cache.get(3))
        println(cache.get(4))
    }
}
