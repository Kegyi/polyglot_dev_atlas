package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

var prev *TreeNode

func inorder(root *TreeNode) {
	if root == nil {
		return
	}
	inorder(root.Left)
	root.Left = nil
	prev.Right = root
	prev = root
	inorder(root.Right)
}

func convertBiNode(root *TreeNode) *TreeNode {
	dummy := &TreeNode{}
	prev = dummy
	inorder(root)
	return dummy.Right
}

func main() {
	root := &TreeNode{Val: 4}
	root.Left = &TreeNode{Val: 2}
	root.Right = &TreeNode{Val: 5}
	root.Left.Left = &TreeNode{Val: 1}
	root.Left.Right = &TreeNode{Val: 3}
	root.Right.Right = &TreeNode{Val: 6}
	root.Left.Left.Left = &TreeNode{Val: 0}

	head := convertBiNode(root)
	for head != nil {
		if head.Right != nil {
			fmt.Printf("%d ", head.Val)
		} else {
			fmt.Printf("%d\n", head.Val)
		}
		head = head.Right
	}
}
