package main

import "fmt"

func isBalanced(s string) bool {
	closeToOpen := map[rune]rune{
		')': '(',
		']': '[',
		'}': '{',
	}

	stack := make([]rune, 0, len(s))
	for _, ch := range s {
		switch ch {
		case '(', '[', '{':
			stack = append(stack, ch)
		case ')', ']', '}':
			if len(stack) == 0 || stack[len(stack)-1] != closeToOpen[ch] {
				return false
			}
			stack = stack[:len(stack)-1]
		}
	}

	return len(stack) == 0
}

func main() {
	input1 := "([{}])(()[]){}"
	input2 := "([)]"

	fmt.Printf("input_1 valid: %v\n", isBalanced(input1))
	fmt.Printf("input_2 valid: %v\n", isBalanced(input2))
}
