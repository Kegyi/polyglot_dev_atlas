object Lcci0105OneAway:
  def oneAway(a: String, b: String): Boolean =
    if (math.abs(a.length - b.length) > 1) {
      return false
    }

    val (s1, s2) = if (a.length <= b.length) (a, b) else (b, a)
    var i = 0
    var j = 0
    var found = false

    while (i < s1.length && j < s2.length) {
      if (s1(i) == s2(j)) {
        i += 1
        j += 1
      } else {
        if (found) {
          return false
        }
        found = true
        if (s1.length == s2.length) {
          i += 1
        }
        j += 1
      }
    }

    true

  @main def main(): Unit =
    println(s"pale vs ple -> ${oneAway("pale", "ple")}")
    println(s"pales vs pale -> ${oneAway("pales", "pale")}")
    println(s"pale vs bake -> ${oneAway("pale", "bake")}")
