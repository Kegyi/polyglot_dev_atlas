package main

import "fmt"

type Node struct {
	Val         int
	Left, Right *Node
}

func heightOrFail(n *Node) int {
	if n == nil {
		return 0
	}
	lh := heightOrFail(n.Left)
	if lh == -1 {
		return -1
	}
	rh := heightOrFail(n.Right)
	if rh == -1 {
		return -1
	}
	if lh-rh > 1 || rh-lh > 1 {
		return -1
	}
	if lh > rh {
		return lh + 1
	}
	return rh + 1
}

func isBalanced(root *Node) bool { return heightOrFail(root) != -1 }

func main() {
	a := &Node{Val: 1, Left: &Node{Val: 2}, Right: &Node{Val: 3}}
	b := &Node{Val: 1, Left: &Node{Val: 2, Left: &Node{Val: 3, Left: &Node{Val: 4}}}}
	fmt.Println(isBalanced(a))
	fmt.Println(isBalanced(b))
}
