interface IVisitor {
    visitCircle(c: Circle): void;
    visitRectangle(r: Rectangle): void;
}

interface IElement {
    accept(visitor: IVisitor): void;
}

class Circle implements IElement {
    accept(visitor: IVisitor): void {
        visitor.visitCircle(this);
    }
    
    draw(): void {
        console.log("Drawing circle");
    }
}

class Rectangle implements IElement {
    accept(visitor: IVisitor): void {
        visitor.visitRectangle(this);
    }
    
    draw(): void {
        console.log("Drawing rectangle");
    }
}

class DrawVisitor implements IVisitor {
    visitCircle(c: Circle): void {
        c.draw();
    }
    
    visitRectangle(r: Rectangle): void {
        r.draw();
    }
}

const circle = new Circle();
const rectangle = new Rectangle();
const visitor = new DrawVisitor();

circle.accept(visitor);
rectangle.accept(visitor);
