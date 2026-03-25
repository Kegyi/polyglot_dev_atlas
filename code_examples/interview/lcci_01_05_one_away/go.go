package main

import "fmt"

func oneAway(a string, b string) bool {
	if len(a)-len(b) > 1 || len(b)-len(a) > 1 {
		return false
	}

	s1, s2 := a, b
	if len(s1) > len(s2) {
		s1, s2 = s2, s1
	}

	i, j := 0, 0
	found := false

	for i < len(s1) && j < len(s2) {
		if s1[i] == s2[j] {
			i++
			j++
			continue
		}

		if found {
			return false
		}
		found = true

		if len(s1) == len(s2) {
			i++
		}
		j++
	}

	return true
}

func main() {
	fmt.Printf("pale vs ple -> %t\n", oneAway("pale", "ple"))
	fmt.Printf("pales vs pale -> %t\n", oneAway("pales", "pale"))
	fmt.Printf("pale vs bake -> %t\n", oneAway("pale", "bake"))
}
