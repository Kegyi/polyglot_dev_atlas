package main

import "fmt"

type Node struct {
	Val         int
	Left, Right *Node
}

func same(a *Node, b *Node) bool {
	if a == nil && b == nil {
		return true
	}
	if a == nil || b == nil {
		return false
	}
	return a.Val == b.Val && same(a.Left, b.Left) && same(a.Right, b.Right)
}

func isSubtree(t1 *Node, t2 *Node) bool {
	if t2 == nil {
		return true
	}
	if t1 == nil {
		return false
	}
	if same(t1, t2) {
		return true
	}
	return isSubtree(t1.Left, t2) || isSubtree(t1.Right, t2)
}

func main() {
	t1 := &Node{Val: 3, Left: &Node{Val: 4, Left: &Node{Val: 1}, Right: &Node{Val: 2}}, Right: &Node{Val: 5}}
	t2 := &Node{Val: 4, Left: &Node{Val: 1}, Right: &Node{Val: 2}}
	t3 := &Node{Val: 4, Left: &Node{Val: 1}, Right: &Node{Val: 3}}
	fmt.Println(isSubtree(t1, t2))
	fmt.Println(isSubtree(t1, t3))
}
