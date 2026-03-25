package main

import "fmt"

type Node struct {
	Val         int
	Left, Right *Node
}

func pathSum(root *Node, target int) int {
	count := map[int]int{0: 1}
	var dfs func(*Node, int) int

	dfs = func(node *Node, prefix int) int {
		if node == nil {
			return 0
		}
		prefix += node.Val
		res := count[prefix-target]
		count[prefix]++
		res += dfs(node.Left, prefix)
		res += dfs(node.Right, prefix)
		count[prefix]--
		return res
	}

	return dfs(root, 0)
}

func main() {
	root := &Node{Val: 10}
	root.Left = &Node{Val: 5, Left: &Node{Val: 3, Left: &Node{Val: 3}, Right: &Node{Val: -2}}, Right: &Node{Val: 2, Right: &Node{Val: 1}}}
	root.Right = &Node{Val: -3, Right: &Node{Val: 11}}
	fmt.Println(pathSum(root, 8))
}
