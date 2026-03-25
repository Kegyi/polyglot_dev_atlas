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

func addTwoNumbers(l1, l2 *ListNode) *ListNode {
	dummy := &ListNode{}
	tail := dummy
	carry := 0

	for l1 != nil || l2 != nil || carry > 0 {
		sum := carry
		if l1 != nil {
			sum += l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			sum += l2.Val
			l2 = l2.Next
		}
		tail.Next = &ListNode{Val: sum % 10}
		tail = tail.Next
		carry = sum / 10
	}

	return dummy.Next
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
	a := buildList([]int{7, 1, 6})
	b := buildList([]int{5, 9, 2})
	c := addTwoNumbers(a, b)
	printList(c)
}
