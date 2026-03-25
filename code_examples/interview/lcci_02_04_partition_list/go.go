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

func partition(head *ListNode, x int) *ListNode {
	lessDummy := &ListNode{}
	greaterDummy := &ListNode{}
	lessTail := lessDummy
	greaterTail := greaterDummy

	for head != nil {
		if head.Val < x {
			lessTail.Next = head
			lessTail = lessTail.Next
		} else {
			greaterTail.Next = head
			greaterTail = greaterTail.Next
		}
		head = head.Next
	}

	greaterTail.Next = nil
	lessTail.Next = greaterDummy.Next
	return lessDummy.Next
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
	head := buildList([]int{3, 5, 8, 5, 10, 2, 1})
	head = partition(head, 5)
	printList(head)
}
