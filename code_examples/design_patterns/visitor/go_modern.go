package main

import "fmt"

// Modern Go Visitor using a type switch.
// No Visitor interface, no Accept method - shapes are plain structs.

type Circle struct{}
type Rectangle struct{}

type Shape interface{ isShape() }

func (Circle) isShape()    {}
func (Rectangle) isShape() {}

// draw is a plain function - no visitor struct needed
func draw(s Shape) {
	switch s.(type) {
	case Circle:
		fmt.Println("Drawing circle")
	case Rectangle:
		fmt.Println("Drawing rectangle")
	default:
		panic("unknown shape")
	}
}

// Second operation - added without touching Shape types
func describe(s Shape) string {
	switch s.(type) {
	case Circle:
		return "it's a circle"
	case Rectangle:
		return "it's a rectangle"
	default:
		return "unknown"
	}
}

func main() {
	shapes := []Shape{Circle{}, Rectangle{}}
	for _, s := range shapes {
		draw(s)
	}
	fmt.Println(describe(Circle{}))
	fmt.Println(describe(Rectangle{}))
}
