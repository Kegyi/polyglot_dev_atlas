package main

import "fmt"

// Modern Go Observer using a slice of function callbacks.
// No Observer interface or struct types needed.

type Subject struct {
	listeners []func(string)
}

func (s *Subject) Subscribe(listener func(string)) {
	s.listeners = append(s.listeners, listener)
}

func (s *Subject) Notify(msg string) {
	for _, l := range s.listeners {
		l(msg)
	}
}

func main() {
	subject := &Subject{}

	subject.Subscribe(func(msg string) {
		fmt.Println("Observer1 received:", msg)
	})
	subject.Subscribe(func(msg string) {
		fmt.Println("Observer2 received:", msg)
	})

	subject.Notify("Event 1")
	subject.Notify("Event 2")
}
