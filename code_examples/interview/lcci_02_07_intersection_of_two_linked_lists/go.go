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

func getIntersectionNode(a, b *ListNode) *ListNode {
	if a == nil || b == nil {
		return nil
	}

	p1, p2 := a, b
	for p1 != p2 {
		if p1 != nil {
			p1 = p1.Next
		} else {
			p1 = b
		}
		if p2 != nil {
			p2 = p2.Next
		} else {
			p2 = a
		}
	}
	return p1
}

func main() {
	common := buildList([]int{8, 10})
	a := buildList([]int{3, 1, 5, 9})
	b := buildList([]int{4, 6})

	tailA := a
	for tailA.Next != nil {
		tailA = tailA.Next
	}
	tailA.Next = common

	tailB := b
	for tailB.Next != nil {
		tailB = tailB.Next
	}
	tailB.Next = common

	node := getIntersectionNode(a, b)
	if node != nil {
		fmt.Println(node.Val)
	} else {
		fmt.Println("null")
	}
}
