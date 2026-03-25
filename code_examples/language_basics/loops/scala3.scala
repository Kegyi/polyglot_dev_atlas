// Scala 3: indentation-based syntax, new while-do form; do-while was removed.
@main def loopsBasics(): Unit =
  val values = Vector(1, 2, 3, 4, 5)

  // Index-based for loop
  for i <- values.indices do
    println(s"for index: $i -> ${values(i)}")

  // For-each with guard
  for v <- values if v != 3 do
    println(s"for each: $v")

  // while loop (new `while cond do body` syntax)
  var i = 0
  while i < values.length && values(i) != 4 do
    println(s"while: ${values(i)}")
    i += 1

  // do-while equivalent in Scala 3 (do-while was removed)
  // Pattern: put side effects + condition in the while block, body is ()
  var c = 0
  while
    println(s"do-while iteration: $c")
    c += 1
    c < 2
  do ()
