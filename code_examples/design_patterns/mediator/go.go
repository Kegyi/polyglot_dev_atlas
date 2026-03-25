package main

import "fmt"

type Mediator interface {
	Notify(sender interface{}, event string)
}

type User struct {
	mediator Mediator
	name     string
}

func (u *User) Send(msg string) {
	fmt.Printf("%s sends: %s\n", u.name, msg)
	u.mediator.Notify(u, msg)
}

func (u *User) Receive(msg string) {
	fmt.Printf("%s receives: %s\n", u.name, msg)
}

type ChatRoom struct {
	user1 *User
	user2 *User
}

func (cr *ChatRoom) AddUsers(u1, u2 *User) {
	cr.user1 = u1
	cr.user2 = u2
}

func (cr *ChatRoom) Notify(sender interface{}, event string) {
	if sender == cr.user1 {
		cr.user2.Receive(event)
	} else {
		cr.user1.Receive(event)
	}
}

func main() {
	room := &ChatRoom{}
	u1 := &User{room, "Alice"}
	u2 := &User{room, "Bob"}

	room.AddUsers(u1, u2)

	u1.Send("Hello!")
	u2.Send("Hi there!")
}
