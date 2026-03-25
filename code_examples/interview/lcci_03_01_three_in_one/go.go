package main

import "fmt"

type TripleInOne struct {
	size int
	data []int
	tops [3]int
}

func NewTripleInOne(stackSize int) *TripleInOne {
	return &TripleInOne{
		size: stackSize,
		data: make([]int, 3*stackSize),
	}
}

func (t *TripleInOne) Push(stackNum int, value int) {
	if t.tops[stackNum] == t.size {
		return
	}
	index := stackNum*t.size + t.tops[stackNum]
	t.data[index] = value
	t.tops[stackNum]++
}

func (t *TripleInOne) Pop(stackNum int) int {
	if t.tops[stackNum] == 0 {
		return -1
	}
	t.tops[stackNum]--
	index := stackNum*t.size + t.tops[stackNum]
	return t.data[index]
}

func (t *TripleInOne) Peek(stackNum int) int {
	if t.tops[stackNum] == 0 {
		return -1
	}
	index := stackNum*t.size + t.tops[stackNum] - 1
	return t.data[index]
}

func (t *TripleInOne) IsEmpty(stackNum int) bool {
	return t.tops[stackNum] == 0
}

func main() {
	s := NewTripleInOne(2)
	s.Push(0, 10)
	s.Push(0, 11)
	s.Push(0, 12)
	s.Push(1, 20)
	fmt.Println(s.Peek(0))
	fmt.Println(s.Pop(0))
	fmt.Println(s.Pop(0))
	fmt.Println(s.Pop(0))
	fmt.Println(s.IsEmpty(1))
}
