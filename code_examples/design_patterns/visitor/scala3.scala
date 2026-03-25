// Modern Scala Visitor using sealed trait ADT + pattern matching (Scala 3)
// No Visitor trait, no accept/visit - shapes are plain ADT cases.
// The compiler enforces exhaustiveness at compile time.

sealed trait Shape
case class Circle()    extends Shape
case class Rectangle() extends Shape

// Operations are plain functions - exhaustive match enforced by the compiler
def draw(shape: Shape): Unit = shape match
  case Circle()    => println("Drawing circle")
  case Rectangle() => println("Drawing rectangle")

// Adding an operation without touching Shape types
def describe(shape: Shape): String = shape match
  case Circle()    => "it's a circle"
  case Rectangle() => "it's a rectangle"

@main def visitorModernExample(): Unit =
  val shapes = List(Circle(), Rectangle())
  shapes.foreach(draw)
  shapes.map(describe).foreach(println)
