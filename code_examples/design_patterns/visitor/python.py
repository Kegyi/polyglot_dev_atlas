from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visit_circle(self, circle: "Circle") -> None:
        pass
    
    @abstractmethod
    def visit_rectangle(self, rectangle: "Rectangle") -> None:
        pass

class Element(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass

class Circle(Element):
    def accept(self, visitor: Visitor) -> None:
        visitor.visit_circle(self)
    
    def draw(self) -> None:
        print("Drawing circle")

class Rectangle(Element):
    def accept(self, visitor: Visitor) -> None:
        visitor.visit_rectangle(self)
    
    def draw(self) -> None:
        print("Drawing rectangle")

class DrawVisitor(Visitor):
    def visit_circle(self, circle: Circle) -> None:
        circle.draw()
    
    def visit_rectangle(self, rectangle: Rectangle) -> None:
        rectangle.draw()

circle = Circle()
rectangle = Rectangle()
visitor = DrawVisitor()

circle.accept(visitor)
rectangle.accept(visitor)
