object BalancedBrackets {
  def isBalanced(s: String): Boolean = {
    val closeToOpen = Map(
      ')' -> '(',
      ']' -> '[',
      '}' -> '{'
    )

    val st = scala.collection.mutable.ArrayBuffer.empty[Char]
    s.foreach { ch =>
      ch match {
        case '(' | '[' | '{' => st += ch
        case ')' | ']' | '}' =>
          if (st.isEmpty || st.last != closeToOpen(ch)) return false
          st.remove(st.size - 1)
        case _ =>
      }
    }
    st.isEmpty
  }

  def main(args: Array[String]): Unit = {
    val input1 = "([{}])(()[]){}"
    val input2 = "([)]"

    println(s"input_1 valid: ${isBalanced(input1)}")
    println(s"input_2 valid: ${isBalanced(input2)}")
  }
}
