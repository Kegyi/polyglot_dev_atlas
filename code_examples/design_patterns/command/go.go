package main

import "fmt"

type Receiver struct{}

func (r *Receiver) TurnOn() {
	fmt.Println("Device is ON")
}

func (r *Receiver) TurnOff() {
	fmt.Println("Device is OFF")
}

type Command interface {
	Execute()
}

type TurnOnCommand struct {
	receiver *Receiver
}

func (c *TurnOnCommand) Execute() {
	c.receiver.TurnOn()
}

type TurnOffCommand struct {
	receiver *Receiver
}

func (c *TurnOffCommand) Execute() {
	c.receiver.TurnOff()
}

type Invoker struct {
	commands []Command
}

func (i *Invoker) AddCommand(cmd Command) {
	i.commands = append(i.commands, cmd)
}

func (i *Invoker) ExecuteAll() {
	for _, cmd := range i.commands {
		cmd.Execute()
	}
}

func main() {
	device := &Receiver{}
	invoker := &Invoker{}

	invoker.AddCommand(&TurnOnCommand{device})
	invoker.AddCommand(&TurnOffCommand{device})

	invoker.ExecuteAll()
}
