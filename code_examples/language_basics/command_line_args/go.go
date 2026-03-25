package main

import (
	"fmt"
	"os"
)

func main() {
	name := "world"
	if len(os.Args) > 1 {
		name = os.Args[1]
	}

	excited := len(os.Args) > 2 && os.Args[2] == "--excited"
	message := fmt.Sprintf("Hello, %s", name)
	if excited {
		message += "!"
	}

	fmt.Println(message)
}
