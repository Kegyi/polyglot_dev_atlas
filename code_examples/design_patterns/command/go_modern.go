package main

import "fmt"

// Modern Go Command using function closures.
// No Command interface or struct types needed.

type Device struct{}

func (d Device) TurnOn()  { fmt.Println("Device is ON") }
func (d Device) TurnOff() { fmt.Println("Device is OFF") }

func main() {
	device := Device{}

	commands := []func(){
		func() { device.TurnOn() },
		func() { device.TurnOff() },
	}

	for _, cmd := range commands {
		cmd()
	}
}
