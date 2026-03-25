package main

import "fmt"

func sortStack(st []int) []int {
	tmp := []int{}
	for len(st) > 0 {
		cur := st[len(st)-1]
		st = st[:len(st)-1]
		for len(tmp) > 0 && tmp[len(tmp)-1] > cur {
			st = append(st, tmp[len(tmp)-1])
			tmp = tmp[:len(tmp)-1]
		}
		tmp = append(tmp, cur)
	}
	for len(tmp) > 0 {
		st = append(st, tmp[len(tmp)-1])
		tmp = tmp[:len(tmp)-1]
	}
	return st
}

func main() {
	st := []int{3, 1, 4, 2}
	st = sortStack(st)
	for i := len(st) - 1; i >= 0; i-- {
		if i != len(st)-1 {
			fmt.Print(" ")
		}
		fmt.Print(st[i])
	}
	fmt.Println()
}
