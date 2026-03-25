package main

import "fmt"

func gradeToLabel(grade int) string {
	if grade >= 90 {
		return "excellent"
	} else if grade >= 75 {
		return "good"
	} else if grade >= 60 {
		return "pass"
	}
	return "fail"
}

func main() {
	grade := 82
	code := 2

	fmt.Println("if/else:", gradeToLabel(grade))

	switch code {
	case 1:
		fmt.Println("switch: created")
	case 2:
		fmt.Println("switch: updated")
	case 3:
		fmt.Println("switch: deleted")
	default:
		fmt.Println("switch: unknown")
	}

	ready := grade >= 60
	if ready {
		fmt.Println("decision: can continue")
	} else {
		fmt.Println("decision: needs retry")
	}
}
