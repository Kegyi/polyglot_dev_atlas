package main

import "fmt"

type GlyphStyle struct {
	font string
}

type StyleFactory struct {
	styles map[string]*GlyphStyle
}

func NewStyleFactory() *StyleFactory {
	return &StyleFactory{styles: map[string]*GlyphStyle{}}
}

func (f *StyleFactory) Get(font string) *GlyphStyle {
	if style, ok := f.styles[font]; ok {
		return style
	}
	style := &GlyphStyle{font: font}
	f.styles[font] = style
	return style
}

func main() {
	factory := NewStyleFactory()
	first := factory.Get("mono-12")
	second := factory.Get("mono-12")
	fmt.Println(first == second)
}
