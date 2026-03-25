package main

import "fmt"

func masterMind(solution string, guess string) []int {
	hits := 0
	cs := make([]int, 26)
	cg := make([]int, 26)
	for i := 0; i < 4; i++ {
		if solution[i] == guess[i] {
			hits++
		} else {
			cs[solution[i]-'A']++
			cg[guess[i]-'A']++
		}
	}
	pseudo := 0
	for i := 0; i < 26; i++ {
		if cs[i] < cg[i] {
			pseudo += cs[i]
		} else {
			pseudo += cg[i]
		}
	}
	return []int{hits, pseudo}
}

func main() {
	fmt.Println(masterMind("RGBY", "GGRR"))
}
