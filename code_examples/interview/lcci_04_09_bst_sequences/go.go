package main

import "fmt"

type Node struct {
	Val         int
	Left, Right *Node
}

func weave(first []int, second []int, prefix []int, out *[][]int) {
	if len(first) == 0 || len(second) == 0 {
		merged := append([]int{}, prefix...)
		merged = append(merged, first...)
		merged = append(merged, second...)
		*out = append(*out, merged)
		return
	}

	weave(first[1:], second, append(append([]int{}, prefix...), first[0]), out)
	weave(first, second[1:], append(append([]int{}, prefix...), second[0]), out)
}

func allSeq(root *Node) [][]int {
	if root == nil {
		return [][]int{{}}
	}
	left := allSeq(root.Left)
	right := allSeq(root.Right)
	result := [][]int{}

	for _, l := range left {
		for _, r := range right {
			weaved := [][]int{}
			weave(l, r, []int{root.Val}, &weaved)
			result = append(result, weaved...)
		}
	}
	return result
}

func main() {
	root := &Node{Val: 2, Left: &Node{Val: 1}, Right: &Node{Val: 3}}
	for _, seq := range allSeq(root) {
		fmt.Println(seq)
	}
}
