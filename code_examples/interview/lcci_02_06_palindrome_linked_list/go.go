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

func reverseList(head *ListNode) *ListNode {
	var prev *ListNode
	for head != nil {
		nextNode := head.Next
		head.Next = prev
		prev = head
		head = nextNode
	}
	return prev
}

func isPalindrome(head *ListNode) bool {
	if head == nil || head.Next == nil {
		return true
	}

	slow, fast := head, head
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}

	second := reverseList(slow)
	p1, p2 := head, second
	for p2 != nil {
		if p1.Val != p2.Val {
			return false
		}
		p1 = p1.Next
		p2 = p2.Next
	}
	return true
}

func main() {
	a := buildList([]int{1, 2, 2, 1})
	b := buildList([]int{1, 2, 3, 2, 1})
	fmt.Println(isPalindrome(a))
	fmt.Println(isPalindrome(b))
}
