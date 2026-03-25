// Visitor
trait Visitor {
    def visitCircle(c: Circle): Unit
    def visitRectangle(r: Rectangle): Unit
}

trait Element {
    def accept(visitor: Visitor): Unit
}

class Circle extends Element {
    def accept(visitor: Visitor): Unit = {
        visitor.visitCircle(this)
    }
    
    def draw(): Unit = println("Drawing circle")
}

class Rectangle extends Element {
    def accept(visitor: Visitor): Unit = {
        visitor.visitRectangle(this)
    }
    
    def draw(): Unit = println("Drawing rectangle")
}

class DrawVisitor extends Visitor {
    def visitCircle(c: Circle): Unit = {
        c.draw()
    }
    
    def visitRectangle(r: Rectangle): Unit = {
        r.draw()
    }
}

object Main extends App {
    val circle = new Circle()
    val rectangle = new Rectangle()
    val visitor = new DrawVisitor()
    
    circle.accept(visitor)
    rectangle.accept(visitor)
}
