object ConditionsBasics:
  def gradeToLabel(grade: Int): String =
    if (grade >= 90) "excellent"
    else if (grade >= 75) "good"
    else if (grade >= 60) "pass"
    else "fail"

  @main def main(): Unit =
    val grade = 82
    val code = 2

    println(s"if/else: ${gradeToLabel(grade)}")

    code match {
      case 1 => println("match: created")
      case 2 => println("match: updated")
      case 3 => println("match: deleted")
      case _ => println("match: unknown")
    }

    val message = if (grade >= 60) "can continue" else "needs retry"
    println(s"if-expression: $message")
