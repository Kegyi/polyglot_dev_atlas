package main

import "fmt"

func main() {
	// Stack: slice used as LIFO
	stack := []int{}
	for _, v := range []int{1, 2, 3} {
		stack = append(stack, v)
	}
	fmt.Println("stack top:", stack[len(stack)-1]) // 3
	stack = stack[:len(stack)-1]
	fmt.Println("after pop:", stack[len(stack)-1]) // 2

	// Queue: slice used as FIFO
	queue := []int{}
	for _, v := range []int{1, 2, 3} {
		queue = append(queue, v)
	}
	fmt.Println("queue front:", queue[0]) // 1
	queue = queue[1:]
	fmt.Println("after dequeue:", queue[0]) // 2
}
