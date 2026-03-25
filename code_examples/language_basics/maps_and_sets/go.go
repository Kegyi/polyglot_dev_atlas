package main

import "fmt"

func main() {
	counts := map[string]int{
		"apple":  2,
		"banana": 1,
	}
	counts["apple"] += 3

	tags := map[string]struct{}{
		"fruit": {},
		"food":  {},
	}
	tags["fresh"] = struct{}{}

	fmt.Println("apple count:", counts["apple"])
	fmt.Println("all map entries:")
	for k, v := range counts {
		fmt.Printf("(%s,%d) ", k, v)
	}
	fmt.Println()

	fmt.Println("all set entries:")
	for t := range tags {
		fmt.Printf("%s ", t)
	}
	fmt.Println()
}
