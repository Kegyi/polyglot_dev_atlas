package main

import "fmt"

func findString(words []string, target string) int {
	left, right := 0, len(words)-1
	answer := -1
	for left <= right {
		mid := (left + right) / 2
		lo, hi := mid, mid
		actual := -1
		for lo >= left || hi <= right {
			if lo >= left && words[lo] != "" {
				actual = lo
				break
			}
			if hi <= right && words[hi] != "" {
				actual = hi
				break
			}
			lo--
			hi++
		}
		if actual == -1 {
			break
		}
		if words[actual] == target {
			answer = actual
			right = actual - 1
		} else if words[actual] < target {
			left = actual + 1
		} else {
			right = actual - 1
		}
	}
	return answer
}

func main() {
	words := []string{"at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""}
	fmt.Println(findString(words, "ta"))
	fmt.Println(findString(words, "ball"))
}
