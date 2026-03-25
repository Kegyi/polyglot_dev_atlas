object Lcci1010RankFromStream {
    final class BinaryIndexedTree(size: Int) {
        private val tree = Array.fill(size + 1)(0)

        def update(index0: Int, delta: Int): Unit = {
            var index = index0
            while (index < tree.length) {
                tree(index) += delta
                index += index & -index
            }
        }

        def query(index0: Int): Int = {
            var index = index0
            var sum = 0
            while (index > 0) {
                sum += tree(index)
                index -= index & -index
            }
            sum
        }
    }

    final class StreamRank {
        private val bit = new BinaryIndexedTree(50010)

        def track(x: Int): Unit = bit.update(x + 1, 1)

        def getRankOfNumber(x: Int): Int = bit.query(x + 1)
    }

    def main(args: Array[String]): Unit = {
        val streamRank = new StreamRank
        println(streamRank.getRankOfNumber(1))
        streamRank.track(0)
        println(streamRank.getRankOfNumber(0))
    }
}
