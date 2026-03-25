package main

import "fmt"

type Node interface {
	TotalSize() int
}

type File struct {
	size int
}

func (f File) TotalSize() int { return f.size }

type Folder struct {
	children []Node
}

func (f *Folder) Add(child Node) {
	f.children = append(f.children, child)
}

func (f Folder) TotalSize() int {
	total := 0
	for _, child := range f.children {
		total += child.TotalSize()
	}
	return total
}

func main() {
	root := &Folder{}
	root.Add(File{size: 5})
	sub := &Folder{}
	sub.Add(File{size: 7})
	sub.Add(File{size: 3})
	root.Add(sub)
	fmt.Println(root.TotalSize())
}
