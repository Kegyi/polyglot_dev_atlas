object Lcci1613BisectSquares {
    def cutSquares(square1: Array[Int], square2: Array[Int]): Array[Double] = {
        val x1 = square1(0).toDouble
        val y1 = square1(1).toDouble
        val s1 = square1(2).toDouble
        val x2 = square2(0).toDouble
        val y2 = square2(1).toDouble
        val s2 = square2(2).toDouble

        val cx1 = x1 + s1 / 2.0
        val cy1 = y1 + s1 / 2.0
        val cx2 = x2 + s2 / 2.0
        val cy2 = y2 + s2 / 2.0

        if (math.abs(cx1 - cx2) < 1e-9) {
            val x = cx1
            val yBottom = math.min(y1, y2)
            val yTop = math.max(y1 + s1, y2 + s2)
            return Array(x, yBottom, x, yTop)
        }

        val k = (cy2 - cy1) / (cx2 - cx1)
        val b = cy1 - k * cx1

        var px1 = 0.0
        var py1 = 0.0
        var px2 = 0.0
        var py2 = 0.0

        if (math.abs(k) <= 1) {
            px1 = math.min(x1, x2)
            px2 = math.max(x1 + s1, x2 + s2)
            py1 = k * px1 + b
            py2 = k * px2 + b
        } else {
            py1 = math.min(y1, y2)
            py2 = math.max(y1 + s1, y2 + s2)
            px1 = (py1 - b) / k
            px2 = (py2 - b) / k
        }

        if (px1 > px2 || (math.abs(px1 - px2) < 1e-9 && py1 > py2)) {
            val tx = px1
            px1 = px2
            px2 = tx
            val ty = py1
            py1 = py2
            py2 = ty
        }

        Array(px1, py1, px2, py2)
    }

    def main(args: Array[String]): Unit = {
        println(cutSquares(Array(-1, -1, 2), Array(0, -1, 2)).mkString("[", ", ", "]"))
    }
}
