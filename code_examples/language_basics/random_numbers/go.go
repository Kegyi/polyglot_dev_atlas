package main

import (
	"fmt"
	"math/rand"
)

func main() {
	generator := rand.New(rand.NewSource(42))
	draws := []int{
		generator.Intn(10) + 1,
		generator.Intn(10) + 1,
		generator.Intn(10) + 1,
	}
	fmt.Println("draws:", draws)
}
