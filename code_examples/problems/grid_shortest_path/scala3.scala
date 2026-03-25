object GridShortestPath:
  private val dirs = List((1, 0), (-1, 0), (0, 1), (0, -1))

  def shortestPathSteps(grid: Vector[Vector[Int]]): Int =
    val rows = grid.length
    val cols = grid.head.length

    if (grid(0)(0) == 1 || grid(rows - 1)(cols - 1) == 1) {
      return -1
    }

    val dist = Array.fill(rows, cols)(-1)
    val q = scala.collection.mutable.Queue[(Int, Int)]()
    q.enqueue((0, 0))
    dist(0)(0) = 0

    while (q.nonEmpty) {
      val (r, c) = q.dequeue()
      if (r == rows - 1 && c == cols - 1) {
        return dist(r)(c)
      }

      dirs.foreach { case (dr, dc) =>
        val nr = r + dr
        val nc = c + dc
        val inBounds = nr >= 0 && nr < rows && nc >= 0 && nc < cols
        if (inBounds && grid(nr)(nc) == 0 && dist(nr)(nc) == -1) {
          dist(nr)(nc) = dist(r)(c) + 1
          q.enqueue((nr, nc))
        }
      }
    }

    -1

  @main def main(): Unit =
    val grid = Vector(
      Vector(0, 0, 1, 0, 0),
      Vector(1, 0, 1, 0, 1),
      Vector(0, 0, 0, 0, 0),
      Vector(0, 1, 1, 1, 0),
      Vector(0, 0, 0, 1, 0)
    )

    println(s"shortest steps: ${shortestPathSteps(grid)}")
