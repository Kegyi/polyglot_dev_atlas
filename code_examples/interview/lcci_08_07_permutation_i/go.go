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
			if !used[i] {
				used[i] = true
				path = append(path, c)
				backtrack()
				path = path[:len(path)-1]
				used[i] = false
			}
		}
	}

	backtrack()
	return result
}

func main() {
	for _, p := range permutation("qwe") {
		fmt.Println(p)
	}
}
