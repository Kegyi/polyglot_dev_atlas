object Lcci1603Intersection:
    private val EPS = 1e-9

    private def lessPoint(a: Array[Double], b: Array[Double]): Boolean = {
        if (math.abs(a(0) - b(0)) > EPS) a(0) < b(0) else a(1) < b(1) - EPS
    }

    private def cross(a: Array[Double], b: Array[Double], c: Array[Double]): Double = {
        (b(0) - a(0)) * (c(1) - a(1)) - (b(1) - a(1)) * (c(0) - a(0))
    }

    private def onSegment(a: Array[Double], b: Array[Double], p: Array[Double]): Boolean = {
        math.abs(cross(a, b, p)) < EPS &&
        math.min(a(0), b(0)) - EPS <= p(0) && p(0) <= math.max(a(0), b(0)) + EPS &&
        math.min(a(1), b(1)) - EPS <= p(1) && p(1) <= math.max(a(1), b(1)) + EPS
    }

    def intersection(start1: Array[Double], end1: Array[Double], start2: Array[Double], end2: Array[Double]): Array[Double] =
        var s1 = start1.clone()
        var e1 = end1.clone()
        var s2 = start2.clone()
        var e2 = end2.clone()

        if (lessPoint(e1, s1)) {
            val t = s1; s1 = e1; e1 = t
        }
        if (lessPoint(e2, s2)) {
            val t = s2; s2 = e2; e2 = t
        }

        val d1 = cross(s1, e1, s2)
        val d2 = cross(s1, e1, e2)
        val d3 = cross(s2, e2, s1)
        val d4 = cross(s2, e2, e1)

        if (((d1 > EPS && d2 > EPS) || (d1 < -EPS && d2 < -EPS)) ||
            ((d3 > EPS && d4 > EPS) || (d3 < -EPS && d4 < -EPS))) {
            return Array.emptyDoubleArray
        }

        val a1 = e1(1) - s1(1)
        val b1 = s1(0) - e1(0)
        val c1 = a1 * s1(0) + b1 * s1(1)

        val a2 = e2(1) - s2(1)
        val b2 = s2(0) - e2(0)
        val c2 = a2 * s2(0) + b2 * s2(1)

        val det = a1 * b2 - a2 * b1
        if (math.abs(det) < EPS) {
            val candidates = scala.collection.mutable.ArrayBuffer[Array[Double]]()
            if (onSegment(s1, e1, s2)) candidates += s2
            if (onSegment(s1, e1, e2)) candidates += e2
            if (onSegment(s2, e2, s1)) candidates += s1
            if (onSegment(s2, e2, e1)) candidates += e1
            if (candidates.isEmpty) return Array.emptyDoubleArray
            val sorted = candidates.sortBy(p => (p(0), p(1)))
            return sorted.head
        }

        val x = (b2 * c1 - b1 * c2) / det
        val y = (a1 * c2 - a2 * c1) / det
        val p = Array(x, y)
        if (onSegment(s1, e1, p) && onSegment(s2, e2, p)) p else Array.emptyDoubleArray

    @main def main(): Unit =
        val ans = intersection(Array(0, 0), Array(1, 0), Array(1, 1), Array(0, -1))
        println(ans.mkString("[", ", ", "]"))
