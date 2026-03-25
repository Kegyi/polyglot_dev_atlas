package main

import "fmt"

func pairSums(nums []int, target int) [][]int {
	freq := map[int]int{}
	ans := make([][]int, 0)
	for _, x := range nums {
		y := target - x
		if freq[y] > 0 {
			freq[y]--
			a, b := x, y
			if a > b {
				a, b = b, a
			}
			ans = append(ans, []int{a, b})
		} else {
			freq[x]++
		}
	}
	return ans
}

func main() {
	fmt.Println(pairSums([]int{5, 6, 5}, 11))
}
