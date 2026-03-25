package main

import (
	"container/heap"
	"fmt"
)

type entry struct {
	count int
	value int
}

type minHeap []entry

func (h minHeap) Len() int { return len(h) }

func (h minHeap) Less(i, j int) bool { return h[i].count < h[j].count }

func (h minHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

func (h *minHeap) Push(x any) {
	*h = append(*h, x.(entry))
}

func (h *minHeap) Pop() any {
	old := *h
	n := len(old)
	out := old[n-1]
	*h = old[:n-1]
	return out
}

func topKFrequent(nums []int, k int) []int {
	freq := map[int]int{}
	for _, n := range nums {
		freq[n]++
	}

	h := &minHeap{}
	heap.Init(h)

	for value, count := range freq {
		heap.Push(h, entry{count: count, value: value})
		if h.Len() > k {
			heap.Pop(h)
		}
	}

	result := make([]int, h.Len())
	for i := len(result) - 1; i >= 0; i-- {
		result[i] = heap.Pop(h).(entry).value
	}
	return result
}

func main() {
	nums := []int{1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 5, 5}
	k := 2
	result := topKFrequent(nums, k)

	fmt.Print("top k frequent:")
	for _, v := range result {
		fmt.Printf(" %d", v)
	}
	fmt.Println()
}
