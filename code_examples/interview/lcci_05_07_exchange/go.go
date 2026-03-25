package main

import "fmt"

func exchangeBits(num int) int {
	u := uint32(num)
	return int(((u & 0xAAAAAAAA) >> 1) | ((u & 0x55555555) << 1))
}

func main() {
	fmt.Println(exchangeBits(2))
	fmt.Println(exchangeBits(3))
}
