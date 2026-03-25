package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	const path = "file_io_demo.txt"

	err := os.WriteFile(path, []byte("apple\nbanana\ncarrot\n"), 0o644)
	if err != nil {
		panic(err)
	}

	content, err := os.ReadFile(path)
	if err != nil {
		panic(err)
	}

	lines := strings.Fields(string(content))
	fmt.Println("read lines:", lines)
}
