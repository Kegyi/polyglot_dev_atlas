package main

import "fmt"

type Memento struct {
	state string
}

func (m *Memento) GetState() string {
	return m.state
}

type Originator struct {
	state string
}

func (o *Originator) SetState(s string) {
	o.state = s
}

func (o *Originator) GetState() string {
	return o.state
}

func (o *Originator) SaveState() *Memento {
	return &Memento{o.state}
}

func (o *Originator) RestoreState(m *Memento) {
	o.state = m.GetState()
}

type Caretaker struct {
	history []*Memento
}

func (c *Caretaker) Save(m *Memento) {
	c.history = append(c.history, m)
}

func (c *Caretaker) Restore(index int) *Memento {
	if index >= 0 && index < len(c.history) {
		return c.history[index]
	}
	return nil
}

func main() {
	origin := &Originator{}
	caretaker := &Caretaker{}

	origin.SetState("State 1")
	caretaker.Save(origin.SaveState())

	origin.SetState("State 2")
	caretaker.Save(origin.SaveState())

	origin.SetState("State 3")
	fmt.Printf("Current: %s\n", origin.GetState())

	origin.RestoreState(caretaker.Restore(0))
	fmt.Printf("Restored: %s\n", origin.GetState())
}
