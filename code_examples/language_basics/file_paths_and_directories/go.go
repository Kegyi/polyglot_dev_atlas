package main

import (
	"fmt"
	"os"
	"path/filepath"
)

func main() {
	base := "demo_folder"
	filePath := filepath.Join(base, "sub", "data.txt")
	parent := filepath.Dir(filePath)

	if err := os.MkdirAll(parent, 0o755); err != nil {
		panic(err)
	}

	fmt.Println("file path:", filePath)
	fmt.Println("parent path:", parent)
	fmt.Println("directory exists:", pathExists(parent))
}

func pathExists(path string) bool {
	_, err := os.Stat(path)
	return err == nil
}
