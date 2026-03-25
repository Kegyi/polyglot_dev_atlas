package main

import "fmt"

func drawLine(length int, w int, x1 int, x2 int, y int) []int {
	wordsPerRow := w / 32
	screen := make([]int, length)
	offset := y * wordsPerRow

	startWord := x1/32 + offset
	endWord := x2/32 + offset
	startBit := x1 % 32
	endBit := x2 % 32

	for i := startWord; i <= endWord; i++ {
		hi := 0xFF
		if i == startWord {
			hi = 0xFF >> startBit
		}
		lo := 0xFF
		if i == endWord {
			lo = ^(0xFF >> (endBit + 1))
		}
		screen[i] = hi & lo
	}
	return screen
}

func main() {
	result := drawLine(1, 32, 1, 30, 0)
	for _, v := range result {
		fmt.Printf("%x\n", v)
	}
}
