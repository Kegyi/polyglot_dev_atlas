package main

import "fmt"

type Node struct {
	Val         int
	Left, Right *Node
}

func listOfDepth(root *Node) [][]int {
	if root == nil {
		return nil
	}
	out := [][]int{}
	q := []*Node{root}
	for len(q) > 0 {
		n := len(q)
		level := []int{}
		for i := 0; i < n; i++ {
			cur := q[0]
			q = q[1:]
			level = append(level, cur.Val)
			if cur.Left != nil {
				q = append(q, cur.Left)
			}
			if cur.Right != nil {
				q = append(q, cur.Right)
			}
		}
		out = append(out, level)
	}
	return out
}

func main() {
	root := &Node{Val: 1}
	root.Left, root.Right = &Node{Val: 2}, &Node{Val: 3}
	root.Left.Left, root.Left.Right = &Node{Val: 4}, &Node{Val: 5}
	root.Right.Left, root.Right.Right = &Node{Val: 6}, &Node{Val: 7}
	levels := listOfDepth(root)
	for i, lvl := range levels {
		if i > 0 {
			fmt.Print(" | ")
		}
		for j, v := range lvl {
			if j > 0 {
				fmt.Print(" ")
			}
			fmt.Print(v)
		}
	}
	fmt.Println()
}
