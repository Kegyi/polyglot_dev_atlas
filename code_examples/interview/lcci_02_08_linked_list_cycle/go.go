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

func hasCycle(head *ListNode) bool {
	slow, fast := head, head
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
		if slow == fast {
			return true
		}
	}
	return false
}

func main() {
	a := buildList([]int{1, 2, 3, 4})
	tail := a
	for tail.Next != nil {
		tail = tail.Next
	}
	tail.Next = a.Next

	b := buildList([]int{1, 2, 3, 4})

	fmt.Println(hasCycle(a))
	fmt.Println(hasCycle(b))
}
