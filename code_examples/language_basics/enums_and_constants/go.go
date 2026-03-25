package main

import "fmt"

type Status int

const (
	Pending Status = iota
	Running
	Done
)

const MaxRetries = 3

func (status Status) String() string {
	switch status {
	case Pending:
		return "pending"
	case Running:
		return "running"
	case Done:
		return "done"
	default:
		return "unknown"
	}
}

func main() {
	status := Running
	fmt.Println("status:", status.String())
	fmt.Println("max retries:", MaxRetries)
}
