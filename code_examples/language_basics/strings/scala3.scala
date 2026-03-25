object StringsBasics:
  @main def main(): Unit =
    val first = "hello"
    val second = "world"
    val joined = s"$first $second"

    val part = joined.substring(0, 5)
    val replaced = joined.replace("hello", "hi")
    val words = joined.split("\\s+").toSeq

    println(s"joined: $joined")
    println(s"part: $part")
    println(s"replaced: $replaced")
    println(s"tokens: $words")
