package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func buildList(nums []int) *ListNode {
	dummy := &ListNode{}
	tail := dummy
	for _, n := range nums {
		tail.Next = &ListNode{Val: n}
		tail = tail.Next
	}
	return dummy.Next
}

func deleteMiddleNode(node *ListNode) bool {
	if node == nil || node.Next == nil {
		return false
	}
	node.Val = node.Next.Val
	node.Next = node.Next.Next
	return true
}

func printList(head *ListNode) {
	first := true
	for head != nil {
		if !first {
			fmt.Print(" ")
		}
		fmt.Print(head.Val)
		first = false
		head = head.Next
	}
	fmt.Println()
}

func main() {
	head := buildList([]int{1, 2, 3, 4, 5})
	deleteMiddleNode(head.Next.Next)
	printList(head)
}
