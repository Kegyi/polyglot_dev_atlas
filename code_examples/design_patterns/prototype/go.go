package main

import "fmt"

type Prototype interface {
	Clone() Prototype
	Describe()
}

type Report struct {
	Title string
	Tags  []string
}

func (r Report) Clone() Prototype {
	tags := append([]string(nil), r.Tags...)
	return Report{Title: r.Title, Tags: tags}
}

func (r Report) Describe() {
	fmt.Printf("%s %v\n", r.Title, r.Tags)
}

func main() {
	template := Report{Title: "weekly", Tags: []string{"ops", "summary"}}
	copy := template.Clone()
	template.Describe()
	copy.Describe()
}
