object Lcci0810ColorFill:
    def floodFill(image: Array[Array[Int]], sr: Int, sc: Int, newColor: Int): Array[Array[Int]] =
        val old = image(sr)(sc)
        if (old == newColor) return image
        val r = image.length; val c = image(0).length

        def dfs(i: Int, j: Int): Unit =
            if (i < 0 || i >= r || j < 0 || j >= c || image(i)(j) != old) return
            image(i)(j) = newColor
            dfs(i + 1, j); dfs(i - 1, j); dfs(i, j + 1); dfs(i, j - 1)

        dfs(sr, sc)
        image

    @main def main(): Unit =
        val image = Array(Array(1,1,1), Array(1,1,0), Array(1,0,1))
        val result = floodFill(image, 1, 1, 2)
        result.foreach(row => println(row.mkString("[", ",", "]")))
