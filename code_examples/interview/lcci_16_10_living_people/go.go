package main

import "fmt"

func maxAliveYear(birth []int, death []int) int {
	diff := make([]int, 102)
	for i := 0; i < len(birth); i++ {
		diff[birth[i]-1900]++
		if death[i]+1 <= 2000 {
			diff[death[i]+1-1900]--
		}
	}

	bestYear := 1900
	alive := 0
	bestAlive := -1
	for i := 0; i <= 100; i++ {
		alive += diff[i]
		if alive > bestAlive {
			bestAlive = alive
			bestYear = 1900 + i
		}
	}
	return bestYear
}

func main() {
	fmt.Println(maxAliveYear([]int{1900, 1901, 1950}, []int{1948, 1951, 2000}))
}
