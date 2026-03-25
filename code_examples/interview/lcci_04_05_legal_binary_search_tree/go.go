package main

import "fmt"

type Node struct {
	Val         int
	Left, Right *Node
}

func isValid(n *Node, lo int64, hi int64) bool {
	if n == nil {
		return true
	}
	v := int64(n.Val)
	if v <= lo || v >= hi {
		return false
	}
	return isValid(n.Left, lo, v) && isValid(n.Right, v, hi)
}

func main() {
	ok := &Node{Val: 5, Left: &Node{Val: 3}, Right: &Node{Val: 7}}
	bad := &Node{Val: 5, Left: &Node{Val: 3, Right: &Node{Val: 6}}, Right: &Node{Val: 7}}
	fmt.Println(isValid(ok, -1<<62, 1<<62))
	fmt.Println(isValid(bad, -1<<62, 1<<62))
}
