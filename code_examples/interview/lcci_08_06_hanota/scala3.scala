import scala.collection.mutable.ArrayBuffer

object Lcci0806Hanota:
    def hanota(A: ArrayBuffer[Int], B: ArrayBuffer[Int], C: ArrayBuffer[Int]): Unit =
        def move(n: Int, src: ArrayBuffer[Int], aux: ArrayBuffer[Int], dst: ArrayBuffer[Int]): Unit =
            if (n == 0) return
            move(n - 1, src, dst, aux)
            dst += src.remove(src.length - 1)
            move(n - 1, aux, src, dst)
        move(A.length, A, B, C)

    @main def main(): Unit =
        val A = ArrayBuffer(2, 1, 0)
        val B = ArrayBuffer[Int]()
        val C = ArrayBuffer[Int]()
        hanota(A, B, C)
        println(s"A: ${A.mkString("[", ",", "]")}")
        println(s"B: ${B.mkString("[", ",", "]")}")
        println(s"C: ${C.mkString("[", ",", "]")}")
