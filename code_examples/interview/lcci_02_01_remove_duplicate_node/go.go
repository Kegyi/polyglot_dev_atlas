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

func removeDuplicateNodes(head *ListNode) {
	seen := map[int]bool{}
	var prev *ListNode
	cur := head

	for cur != nil {
		if seen[cur.Val] {
			prev.Next = cur.Next
			cur = cur.Next
			continue
		}
		seen[cur.Val] = true
		prev = cur
		cur = cur.Next
	}
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
	head := buildList([]int{1, 2, 3, 3, 2, 1, 4})
	removeDuplicateNodes(head)
	printList(head)
}
