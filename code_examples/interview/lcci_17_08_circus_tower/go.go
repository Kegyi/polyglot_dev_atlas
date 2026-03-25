package main

import (
	"fmt"
	"sort"
)

func bestSeqAtIndex(height []int, weight []int) int {
	type pair struct{ h, w int }
	people := make([]pair, len(height))
	for i := range height {
		people[i] = pair{height[i], weight[i]}
	}
	sort.Slice(people, func(i, j int) bool {
		if people[i].h != people[j].h {
			return people[i].h < people[j].h
		}
		return people[i].w > people[j].w
	})

	lis := []int{}
	for _, p := range people {
		i := sort.SearchInts(lis, p.w)
		if i == len(lis) {
			lis = append(lis, p.w)
		} else {
			lis[i] = p.w
		}
	}
	return len(lis)
}

func main() {
	fmt.Println(bestSeqAtIndex([]int{65, 70, 56, 75, 60, 68}, []int{100, 150, 90, 190, 95, 110})) // 6
	fmt.Println(bestSeqAtIndex([]int{65, 70, 56, 75}, []int{100, 150, 90, 190}))                  // 4
}
