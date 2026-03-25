package main

import (
	"crypto/sha256"
	"fmt"
	"hash/crc32"
)

func main() {
	text := "hello-world"
	bytes := []byte(text)

	sha256Sum := sha256.Sum256(bytes)
	crc32Value := crc32.ChecksumIEEE(bytes)

	fmt.Println("text:", text)
	fmt.Printf("sha256: %x\n", sha256Sum)
	fmt.Println("crc32:", crc32Value)
}
