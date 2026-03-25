package main

import "fmt"

type Speaker interface {
	Speak() string
}

type Dog struct{}

type Cat struct{}

func (Dog) Speak() string {
	return "woof"
}

func (Cat) Speak() string {
	return "meow"
}

func main() {
	speakers := []Speaker{Dog{}, Cat{}}
	for _, speaker := range speakers {
		fmt.Println(speaker.Speak())
	}
}
