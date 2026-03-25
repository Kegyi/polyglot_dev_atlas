object Lcci0109StringRotation:
  def isStringRotation(s1: String, s2: String): Boolean =
    s1.length == s2.length && (s1 + s1).contains(s2)

  @main def main(): Unit =
    println(s"waterbottle vs erbottlewat -> ${isStringRotation("waterbottle", "erbottlewat")}")
    println(s"aa vs aba -> ${isStringRotation("aa", "aba")}")
