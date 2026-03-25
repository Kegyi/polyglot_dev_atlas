package main

import (
	"fmt"
	"sort"
)

func permutation(S string) []string {
	chars := []byte(S)
	sort.Slice(chars, func(i, j int) bool { return chars[i] < chars[j] })
	result := []string{}
	used := make([]bool, len(chars))
	path := []byte{}

	var backtrack func()
	backtrack = func() {
		if len(path) == len(chars) {
			result = append(result, string(path))
			return
		}
		for i, c := range chars {
			if used[i] {
				continue
			}
			if i > 0 && chars[i] == chars[i-1] && !used[i-1] {
				continue
			}
			used[i] = true
			path = append(path, c)
			backtrack()
			path = path[:len(path)-1]
			used[i] = false
		}
	}

	backtrack()
	return result
}

func main() {
	for _, p := range permutation("qqe") {
		fmt.Println(p)
	}
}
