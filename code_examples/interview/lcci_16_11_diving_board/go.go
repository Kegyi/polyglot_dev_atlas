package main

import "fmt"

func divingBoard(shorter int, longer int, k int) []int {
	if k == 0 {
		return []int{}
	}
	if shorter == longer {
		return []int{shorter * k}
	}
	ans := make([]int, 0, k+1)
	for i := 0; i <= k; i++ {
		ans = append(ans, shorter*(k-i)+longer*i)
	}
	return ans
}

func main() {
	fmt.Println(divingBoard(1, 2, 3))
}
