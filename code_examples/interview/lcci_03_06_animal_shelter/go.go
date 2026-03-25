package main

import "fmt"

type Animal struct {
	order int
	id    int
}

type AnimalShelter struct {
	ticket int
	dogs   []Animal
	cats   []Animal
}

func (s *AnimalShelter) Enqueue(id int, kind string) {
	item := Animal{order: s.ticket, id: id}
	s.ticket++
	if kind == "dog" {
		s.dogs = append(s.dogs, item)
	} else {
		s.cats = append(s.cats, item)
	}
}

func (s *AnimalShelter) DequeueAny() int {
	if len(s.dogs) == 0 && len(s.cats) == 0 {
		return -1
	}
	if len(s.dogs) == 0 {
		return s.DequeueCat()
	}
	if len(s.cats) == 0 {
		return s.DequeueDog()
	}
	if s.dogs[0].order < s.cats[0].order {
		return s.DequeueDog()
	}
	return s.DequeueCat()
}

func (s *AnimalShelter) DequeueDog() int {
	if len(s.dogs) == 0 {
		return -1
	}
	id := s.dogs[0].id
	s.dogs = s.dogs[1:]
	return id
}

func (s *AnimalShelter) DequeueCat() int {
	if len(s.cats) == 0 {
		return -1
	}
	id := s.cats[0].id
	s.cats = s.cats[1:]
	return id
}

func main() {
	s := &AnimalShelter{}
	s.Enqueue(1, "dog")
	s.Enqueue(2, "cat")
	s.Enqueue(3, "dog")
	fmt.Println(s.DequeueAny())
	fmt.Println(s.DequeueCat())
	fmt.Println(s.DequeueDog())
	fmt.Println(s.DequeueAny())
}
