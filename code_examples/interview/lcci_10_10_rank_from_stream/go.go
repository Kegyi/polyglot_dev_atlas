package main

import "fmt"

type binaryIndexedTree struct {
	tree []int
}

func newBinaryIndexedTree(n int) *binaryIndexedTree {
	return &binaryIndexedTree{tree: make([]int, n+1)}
}

func (b *binaryIndexedTree) update(index int, delta int) {
	for index < len(b.tree) {
		b.tree[index] += delta
		index += index & -index
	}
}

func (b *binaryIndexedTree) query(index int) int {
	sum := 0
	for index > 0 {
		sum += b.tree[index]
		index -= index & -index
	}
	return sum
}

type StreamRank struct {
	bit *binaryIndexedTree
}

func Constructor() StreamRank {
	return StreamRank{bit: newBinaryIndexedTree(50010)}
}

func (s *StreamRank) Track(x int) {
	s.bit.update(x+1, 1)
}

func (s *StreamRank) GetRankOfNumber(x int) int {
	return s.bit.query(x + 1)
}

func main() {
	streamRank := Constructor()
	fmt.Println(streamRank.GetRankOfNumber(1))
	streamRank.Track(0)
	fmt.Println(streamRank.GetRankOfNumber(0))
}
