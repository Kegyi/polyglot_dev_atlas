package main

import "fmt"

type Observer interface {
	Update(msg string)
}

type Subject struct {
	observers []Observer
}

func (s *Subject) Attach(observer Observer) {
	s.observers = append(s.observers, observer)
}

func (s *Subject) Notify(msg string) {
	for _, observer := range s.observers {
		observer.Update(msg)
	}
}

type ConcreteObserver struct {
	name string
}

func (c *ConcreteObserver) Update(msg string) {
	fmt.Printf("%s received: %s\n", c.name, msg)
}

func main() {
	subject := &Subject{}
	obs1 := &ConcreteObserver{"Observer1"}
	obs2 := &ConcreteObserver{"Observer2"}

	subject.Attach(obs1)
	subject.Attach(obs2)

	subject.Notify("Event 1")
	subject.Notify("Event 2")
}
