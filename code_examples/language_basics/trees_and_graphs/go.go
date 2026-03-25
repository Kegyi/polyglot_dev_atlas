package main

import "fmt"

type TreeNode struct {
	value       int
	left, right *TreeNode
}

func insert(root *TreeNode, value int) *TreeNode {
	if root == nil {
		return &TreeNode{value: value}
	}
	if value < root.value {
		root.left = insert(root.left, value)
	} else {
		root.right = insert(root.right, value)
	}
	return root
}

func inOrder(root *TreeNode) {
	if root == nil {
		return
	}
	inOrder(root.left)
	fmt.Print(root.value, " ")
	inOrder(root.right)
}

func bfs(root *TreeNode) {
	if root == nil {
		return
	}
	queue := []*TreeNode{root}
	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:]
		fmt.Print(node.value, " ")
		if node.left != nil {
			queue = append(queue, node.left)
		}
		if node.right != nil {
			queue = append(queue, node.right)
		}
	}
}

func main() {
	var root *TreeNode
	for _, v := range []int{5, 3, 7, 1, 4} {
		root = insert(root, v)
	}
	fmt.Print("in-order: ")
	inOrder(root)
	fmt.Println() // 1 3 4 5 7
	fmt.Print("bfs:      ")
	bfs(root)
	fmt.Println() // 5 3 7 1 4
}
