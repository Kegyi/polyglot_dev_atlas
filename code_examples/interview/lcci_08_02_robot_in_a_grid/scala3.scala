import scala.collection.mutable.ArrayBuffer

object Lcci0802RobotInAGrid:
    def pathWithObstacles(obstacleGrid: Array[Array[Int]]): Array[Array[Int]] =
        val r = obstacleGrid.length; val c = obstacleGrid(0).length
        val path = ArrayBuffer[Array[Int]]()
        val visited = Array.ofDim[Boolean](r, c)

        def dfs(i: Int, j: Int): Boolean =
            if (i >= r || j >= c || obstacleGrid(i)(j) == 1 || visited(i)(j)) return false
            visited(i)(j) = true
            path += Array(i, j)
            if (i == r - 1 && j == c - 1) return true
            if (dfs(i + 1, j) || dfs(i, j + 1)) return true
            path.remove(path.length - 1)
            false

        dfs(0, 0)
        path.toArray

    @main def main(): Unit =
        val grid = Array(Array(0,0,0), Array(0,1,0), Array(0,0,0))
        val path = pathWithObstacles(grid)
        println(path.map(p => s"[${p(0)},${p(1)}]").mkString("[", ",", "]"))
