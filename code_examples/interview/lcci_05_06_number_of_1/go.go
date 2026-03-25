package main

import (
	"fmt"
	"math/bits"
)

func convertInteger(A int32, B int32) int {
	return bits.OnesCount32(uint32(A ^ B))
}

func main() {
	fmt.Println(convertInteger(29, 15))
	fmt.Println(convertInteger(1, 5))
}
