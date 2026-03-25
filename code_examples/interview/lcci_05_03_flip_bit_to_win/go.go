package main

import "fmt"

func flipBit(num uint32) int {
	if num == 0xFFFFFFFF {
		return 32
	}
	cur, prev, best := 0, 0, 1
	for num > 0 {
		if num&1 == 1 {
			cur++
		} else {
			prev = cur
			cur = 0
		}
		if v := prev + 1 + cur; v > best {
			best = v
		}
		num >>= 1
	}
	return best
}

func main() {
	fmt.Println(flipBit(1775))
	fmt.Println(flipBit(7))
}
