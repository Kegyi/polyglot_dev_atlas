package main

import "fmt"

type StackOfPlates struct {
	cap    int
	stacks [][]int
}

func NewStackOfPlates(capacity int) *StackOfPlates {
	return &StackOfPlates{cap: capacity}
}

func (s *StackOfPlates) Push(val int) {
	if s.cap <= 0 {
		return
	}
	if len(s.stacks) == 0 || len(s.stacks[len(s.stacks)-1]) == s.cap {
		s.stacks = append(s.stacks, []int{})
	}
	last := len(s.stacks) - 1
	s.stacks[last] = append(s.stacks[last], val)
}

func (s *StackOfPlates) Pop() int {
	return s.PopAt(len(s.stacks) - 1)
}

func (s *StackOfPlates) PopAt(index int) int {
	if index < 0 || index >= len(s.stacks) || len(s.stacks[index]) == 0 {
		return -1
	}
	last := len(s.stacks[index]) - 1
	val := s.stacks[index][last]
	s.stacks[index] = s.stacks[index][:last]
	if len(s.stacks[index]) == 0 {
		s.stacks = append(s.stacks[:index], s.stacks[index+1:]...)
	}
	return val
}

func main() {
	s := NewStackOfPlates(2)
	s.Push(1)
	s.Push(2)
	s.Push(3)
	s.Push(4)
	fmt.Println(s.PopAt(0))
	fmt.Println(s.Pop())
	fmt.Println(s.Pop())
	fmt.Println(s.Pop())
}
