package main

import "fmt"

func mapDigit(ch byte) byte {
	switch {
	case ch <= 'c':
		return '2'
	case ch <= 'f':
		return '3'
	case ch <= 'i':
		return '4'
	case ch <= 'l':
		return '5'
	case ch <= 'o':
		return '6'
	case ch <= 's':
		return '7'
	case ch <= 'v':
		return '8'
	default:
		return '9'
	}
}

func getValidT9Words(num string, words []string) []string {
	ans := make([]string, 0)
	for _, word := range words {
		if len(word) != len(num) {
			continue
		}
		ok := true
		for i := 0; i < len(word); i++ {
			if mapDigit(word[i]) != num[i] {
				ok = false
				break
			}
		}
		if ok {
			ans = append(ans, word)
		}
	}
	return ans
}

func main() {
	fmt.Println(getValidT9Words("8733", []string{"tree", "used", "true"}))
}
