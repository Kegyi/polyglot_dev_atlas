package main

import "fmt"

type State interface {
	Handle()
}

type StartState struct{}

func (s *StartState) Handle() {
	fmt.Println("Entering start state")
}

type RunningState struct{}

func (s *RunningState) Handle() {
	fmt.Println("Running state active")
}

type StoppedState struct{}

func (s *StoppedState) Handle() {
	fmt.Println("Stopped state active")
}

type Context struct {
	state State
}

func (c *Context) SetState(s State) {
	c.state = s
}

func (c *Context) Request() {
	c.state.Handle()
}

func main() {
	ctx := &Context{}

	ctx.SetState(&StartState{})
	ctx.Request()

	ctx.SetState(&RunningState{})
	ctx.Request()

	ctx.SetState(&StoppedState{})
	ctx.Request()
}
