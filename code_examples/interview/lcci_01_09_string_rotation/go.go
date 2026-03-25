package main

import (
	"fmt"
	"strings"
)

func isStringRotation(s1 string, s2 string) bool {
	return len(s1) == len(s2) && strings.Contains(s1+s1, s2)
}

func main() {
	fmt.Printf("waterbottle vs erbottlewat -> %t\n", isStringRotation("waterbottle", "erbottlewat"))
	fmt.Printf("aa vs aba -> %t\n", isStringRotation("aa", "aba"))
}
