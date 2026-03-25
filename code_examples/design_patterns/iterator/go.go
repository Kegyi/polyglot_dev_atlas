package main

import "fmt"

type Iterator interface {
	HasNext() bool
	Next() int
}

type Collection interface {
	CreateIterator() Iterator
}

type ArrayIterator struct {
	items    []int
	position int
}

func (i *ArrayIterator) HasNext() bool {
	return i.position < len(i.items)
}

func (i *ArrayIterator) Next() int {
	result := i.items[i.position]
	i.position++
	return result
}

type ArrayCollection struct {
	items []int
}

func (c *ArrayCollection) Add(item int) {
	c.items = append(c.items, item)
}

func (c *ArrayCollection) CreateIterator() Iterator {
	return &ArrayIterator{c.items, 0}
}

func main() {
	collection := &ArrayCollection{}
	collection.Add(10)
	collection.Add(20)
	collection.Add(30)

	it := collection.CreateIterator()
	for it.HasNext() {
		fmt.Printf("%d ", it.Next())
	}
	fmt.Println()
}
