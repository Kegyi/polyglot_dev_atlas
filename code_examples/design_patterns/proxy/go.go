package main

import "fmt"

type Image interface {
	Display()
}

type RealImage struct{}

func NewRealImage() *RealImage {
	fmt.Println("load image")
	return &RealImage{}
}

func (RealImage) Display() {
	fmt.Println("display image")
}

type ImageProxy struct {
	real *RealImage
}

func (p *ImageProxy) Display() {
	if p.real == nil {
		p.real = NewRealImage()
	}
	p.real.Display()
}

func main() {
	proxy := &ImageProxy{}
	proxy.Display()
	proxy.Display()
}
