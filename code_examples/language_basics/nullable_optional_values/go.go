package main

import "fmt"

func parseAge(text string) *int {
	if text == "" {
		return nil
	}

	age := 29
	return &age
}

func main() {
	age := parseAge("29")
	missing := parseAge("")

	fmt.Println("age present:", age != nil)
	if missing == nil {
		fmt.Println("missing default:", 0)
	} else {
		fmt.Println("missing default:", *missing)
	}
}
