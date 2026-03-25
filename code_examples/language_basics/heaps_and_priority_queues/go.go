package main

import (
	"container/heap"
	"fmt"
)

// MinHeap implements heap.Interface for int
type MinHeap []int

func (h MinHeap) Len() int           { return len(h) }
func (h MinHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h MinHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *MinHeap) Push(v any)        { *h = append(*h, v.(int)) }
func (h *MinHeap) Pop() any          { old := *h; n := len(old); v := old[n-1]; *h = old[:n-1]; return v }

func main() {
	data := []int{3, 1, 4, 1, 5, 9}

	// max via negation
	maxH := &MinHeap{}
	for _, v := range data {
		heap.Push(maxH, -v)
	}
	fmt.Println("max:", -(*maxH)[0]) // 9

	// min-heap
	minH := &MinHeap{}
	for _, v := range data {
		heap.Push(minH, v)
	}
	fmt.Print("drain min-heap: ")
	for minH.Len() > 0 {
		fmt.Print(heap.Pop(minH).(int), " ")
	}
	fmt.Println() // 1 1 3 4 5 9
}
