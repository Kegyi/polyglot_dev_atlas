package main

import "fmt"

type Node struct {
	Val         int
	Left, Right *Node
}

func lca(root *Node, p int, q int) *Node {
	if root == nil || root.Val == p || root.Val == q {
		return root
	}
	left := lca(root.Left, p, q)
	right := lca(root.Right, p, q)
	if left != nil && right != nil {
		return root
	}
	if left != nil {
		return left
	}
	return right
}

func main() {
	root := &Node{Val: 3}
	root.Left = &Node{Val: 5, Left: &Node{Val: 6}, Right: &Node{Val: 2}}
	root.Right = &Node{Val: 1, Left: &Node{Val: 0}, Right: &Node{Val: 8}}

	fmt.Println(lca(root, 6, 2).Val)
	fmt.Println(lca(root, 6, 8).Val)
}
