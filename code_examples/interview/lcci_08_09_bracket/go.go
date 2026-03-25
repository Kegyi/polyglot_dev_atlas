package main

import "fmt"

func generateParenthesis(n int) []string {
	result := []string{}

	var bt func(cur string, open, close int)
	bt = func(cur string, open, close int) {
		if len(cur) == 2*n {
			result = append(result, cur)
			return
		}
		if open < n {
			bt(cur+"(", open+1, close)
		}
		if close < open {
			bt(cur+")", open, close+1)
		}
	}

	bt("", 0, 0)
	return result
}

func main() {
	for _, s := range generateParenthesis(3) {
		fmt.Println(s)
	}
}
