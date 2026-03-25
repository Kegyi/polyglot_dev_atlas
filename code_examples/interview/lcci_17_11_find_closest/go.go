package main

import "fmt"

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func findClosest(words []string, word1 string, word2 string) int {
	i1, i2, ans := -1, -1, 1<<30
	for i, w := range words {
		if w == word1 {
			i1 = i
		}
		if w == word2 {
			i2 = i
		}
		if i1 != -1 && i2 != -1 {
			d := abs(i1 - i2)
			if d < ans {
				ans = d
			}
		}
	}
	return ans
}

func main() {
	fmt.Println(findClosest([]string{"I", "am", "a", "student", "from", "a", "university", "in", "a", "city"}, "a", "student")) // 1
	fmt.Println(findClosest([]string{"aa", "bb"}, "aa", "bb"))                                                                  // 1
}
