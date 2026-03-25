package main

import "fmt"

type Node struct {
	Val         int
	Left, Right *Node
}

func inorderSuccessor(root *Node, p int) *Node {
	var ans *Node
	for root != nil {
		if p < root.Val {
			ans = root
			root = root.Left
		} else {
			root = root.Right
		}
	}
	return ans
}

func main() {
	root := &Node{Val: 5, Left: &Node{Val: 3, Left: &Node{Val: 2}, Right: &Node{Val: 4}}, Right: &Node{Val: 7}}
	s1 := inorderSuccessor(root, 3)
	s2 := inorderSuccessor(root, 7)
	if s1 != nil {
		fmt.Println(s1.Val)
	} else {
		fmt.Println(-1)
	}
	if s2 != nil {
		fmt.Println(s2.Val)
	} else {
		fmt.Println(-1)
	}
}
