package main

import "fmt"

func countBits(n int) int {
	count := 0
	for n != 0 {
		count += n & 1
		n >>= 1
	}
	return count
}

func main() {
	a, b := 0b1010, 0b1100            // 10, 12
	fmt.Printf("a & b:  %04b\n", a&b) // 1000
	fmt.Printf("a | b:  %04b\n", a|b) // 1110
	fmt.Printf("a ^ b:  %04b\n", a^b) // 0110

	n := 0b0101
	fmt.Printf("bit 1 set? %d\n", (n>>1)&1)  // check -> 0
	n |= (1 << 2)                            // set bit 2
	n &^= (1 << 0)                           // clear bit 0
	fmt.Printf("after set/clear: %04b\n", n) // 0100

	fmt.Println("count bits in 7:", countBits(7)) // 3
}
