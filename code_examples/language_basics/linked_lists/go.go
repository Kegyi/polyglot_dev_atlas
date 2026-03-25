package main

import "fmt"

type Node struct {
	value int
	next  *Node
}

func printList(head *Node) {
	for cur := head; cur != nil; cur = cur.next {
		fmt.Print(cur.value)
		if cur.next != nil {
			fmt.Print(" -> ")
		}
	}
	fmt.Println()
}

func prepend(head *Node, value int) *Node {
	return &Node{value: value, next: head}
}

func removeValue(head *Node, value int) *Node {
	if head == nil {
		return nil
	}
	if head.value == value {
		return head.next
	}
	head.next = removeValue(head.next, value)
	return head
}

func main() {
	var head *Node
	for _, v := range []int{3, 2, 1} {
		head = prepend(head, v) // 1 -> 2 -> 3
	}
	printList(head)
	head = removeValue(head, 2)
	printList(head) // 1 -> 3
}
