package main

import "fmt"

type WordsFrequency struct {
	counter map[string]int
}

func Constructor(book []string) WordsFrequency {
	counter := map[string]int{}
	for _, word := range book {
		counter[word]++
	}
	return WordsFrequency{counter: counter}
}

func (w *WordsFrequency) Get(word string) int {
	return w.counter[word]
}

func main() {
	wf := Constructor([]string{"i", "have", "an", "apple", "he", "have", "a", "pen"})
	fmt.Println(wf.Get("have"))
	fmt.Println(wf.Get("you"))
}
