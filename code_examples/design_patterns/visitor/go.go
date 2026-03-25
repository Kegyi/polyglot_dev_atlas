package main

import "fmt"

type Visitor interface {
	VisitCircle(*Circle)
	VisitRectangle(*Rectangle)
}

type Element interface {
	Accept(Visitor)
}

type Circle struct{}

func (c *Circle) Accept(v Visitor) {
	v.VisitCircle(c)
}

func (c *Circle) Draw() {
	fmt.Println("Drawing circle")
}

type Rectangle struct{}

func (r *Rectangle) Accept(v Visitor) {
	v.VisitRectangle(r)
}

func (r *Rectangle) Draw() {
	fmt.Println("Drawing rectangle")
}

type DrawVisitor struct{}

func (dv *DrawVisitor) VisitCircle(c *Circle) {
	c.Draw()
}

func (dv *DrawVisitor) VisitRectangle(r *Rectangle) {
	r.Draw()
}

func main() {
	circle := &Circle{}
	rectangle := &Rectangle{}
	visitor := &DrawVisitor{}

	circle.Accept(visitor)
	rectangle.Accept(visitor)
}
