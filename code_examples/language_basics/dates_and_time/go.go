package main

import (
	"fmt"
	"time"
)

func main() {
	now := time.Now()
	later := now.Add(90 * time.Minute)

	fmt.Println("now:", now.Format(time.RFC3339))
	fmt.Println("later:", later.Format(time.RFC3339))
	fmt.Println("later > now:", later.After(now))
}
