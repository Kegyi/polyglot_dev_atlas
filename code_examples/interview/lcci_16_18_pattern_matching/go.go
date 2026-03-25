package main

import "fmt"

func patternMatching(pattern string, value string) bool {
	if pattern == "" {
		return value == ""
	}

	countA, countB := 0, 0
	for i := 0; i < len(pattern); i++ {
		if pattern[i] == 'a' {
			countA++
		} else {
			countB++
		}
	}

	if countA < countB {
		swapped := make([]byte, len(pattern))
		for i := 0; i < len(pattern); i++ {
			if pattern[i] == 'a' {
				swapped[i] = 'b'
			} else {
				swapped[i] = 'a'
			}
		}
		return patternMatching(string(swapped), value)
	}

	if value == "" {
		return countB == 0
	}

	n := len(value)
	for lenA := 0; countA*lenA <= n; lenA++ {
		rest := n - countA*lenA
		lenB := 0
		if countB == 0 {
			if rest != 0 {
				continue
			}
		} else {
			if rest%countB != 0 {
				continue
			}
			lenB = rest / countB
		}

		pos := 0
		a, b := "", ""
		hasA, hasB := false, false
		ok := true
		for i := 0; i < len(pattern); i++ {
			if pattern[i] == 'a' {
				sub := value[pos : pos+lenA]
				if !hasA {
					a = sub
					hasA = true
				} else if a != sub {
					ok = false
					break
				}
				pos += lenA
			} else {
				sub := value[pos : pos+lenB]
				if !hasB {
					b = sub
					hasB = true
				} else if b != sub {
					ok = false
					break
				}
				pos += lenB
			}
		}
		if ok && a != b {
			return true
		}
	}
	return false
}

func main() {
	fmt.Println(patternMatching("abba", "dogcatcatdog"))
	fmt.Println(patternMatching("abba", "dogcatcatfish"))
}
