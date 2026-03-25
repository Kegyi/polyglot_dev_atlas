package main

import "fmt"

type Node struct {
	Val         int
	Left, Right *Node
}

func build(a []int, lo int, hi int) *Node {
	if lo > hi {
		return nil
	}
	mid := (lo + hi) / 2
	root := &Node{Val: a[mid]}
	root.Left = build(a, lo, mid-1)
	root.Right = build(a, mid+1, hi)
	return root
}

func inorder(n *Node, out *[]int) {
	if n == nil {
		return
	}
	inorder(n.Left, out)
	*out = append(*out, n.Val)
	inorder(n.Right, out)
}

func main() {
	nums := []int{1, 2, 3, 4, 5, 6, 7}
	root := build(nums, 0, len(nums)-1)
	out := []int{}
	inorder(root, &out)
	for i, v := range out {
		if i > 0 {
			fmt.Print(" ")
		}
		fmt.Print(v)
	}
	fmt.Println()
}
