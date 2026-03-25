package main

import "fmt"

type MyQueue struct {
	inStack  []int
	outStack []int
}

func (q *MyQueue) Push(x int) {
	q.inStack = append(q.inStack, x)
}

func (q *MyQueue) moveIfNeeded() {
	if len(q.outStack) > 0 {
		return
	}
	for len(q.inStack) > 0 {
		n := len(q.inStack) - 1
		q.outStack = append(q.outStack, q.inStack[n])
		q.inStack = q.inStack[:n]
	}
}

func (q *MyQueue) Pop() int {
	q.moveIfNeeded()
	if len(q.outStack) == 0 {
		return -1
	}
	n := len(q.outStack) - 1
	v := q.outStack[n]
	q.outStack = q.outStack[:n]
	return v
}

func (q *MyQueue) Peek() int {
	q.moveIfNeeded()
	if len(q.outStack) == 0 {
		return -1
	}
	return q.outStack[len(q.outStack)-1]
}

func (q *MyQueue) Empty() bool {
	return len(q.inStack) == 0 && len(q.outStack) == 0
}

func main() {
	q := &MyQueue{}
	q.Push(1)
	q.Push(2)
	q.Push(3)
	fmt.Println(q.Peek())
	fmt.Println(q.Pop())
	fmt.Println(q.Pop())
	fmt.Println(q.Empty())
}
