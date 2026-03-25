package main

import (
	"fmt"
	"strconv"
)

func parsePort(value string) (int, error) {
	return strconv.Atoi(value)
}

func main() {
	port, err := parsePort("not-a-number")
	if err != nil {
		fmt.Println("parse failed:", err)
		fmt.Println("fallback port:", 8080)
	} else {
		fmt.Println("port:", port)
	}

	fmt.Println("program continues")
}
