package main

import "fmt"

type MinStack struct {
	values []int
	mins   []int
}

func (m *MinStack) Push(x int) {
	m.values = append(m.values, x)
	if len(m.mins) == 0 || x <= m.mins[len(m.mins)-1] {
		m.mins = append(m.mins, x)
	}
}

func (m *MinStack) Pop() {
	if len(m.values) == 0 {
		return
	}
	top := m.values[len(m.values)-1]
	if top == m.mins[len(m.mins)-1] {
		m.mins = m.mins[:len(m.mins)-1]
	}
	m.values = m.values[:len(m.values)-1]
}

func (m *MinStack) Top() int {
	if len(m.values) == 0 {
		return -1
	}
	return m.values[len(m.values)-1]
}

func (m *MinStack) GetMin() int {
	if len(m.mins) == 0 {
		return -1
	}
	return m.mins[len(m.mins)-1]
}

func main() {
	st := &MinStack{}
	st.Push(3)
	st.Push(5)
	st.Push(2)
	st.Push(2)
	fmt.Println(st.GetMin())
	st.Pop()
	fmt.Println(st.GetMin())
	st.Pop()
	fmt.Println(st.GetMin())
}
