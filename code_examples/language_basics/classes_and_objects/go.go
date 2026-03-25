package main

import "fmt"

type Person struct {
	Name string
	Age  int
}

func (person Person) Describe() string {
	return fmt.Sprintf("%s is %d years old", person.Name, person.Age)
}

func (person *Person) Birthday() {
	person.Age++
}

func main() {
	person := Person{Name: "Alice", Age: 29}
	fmt.Println(person.Describe())
	person.Birthday()
	fmt.Println(person.Describe())
}
