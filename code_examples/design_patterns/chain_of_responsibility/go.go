package main

import (
	"fmt"
)

type Request struct {
	level   int
	message string
}

type Handler interface {
	SetNext(Handler)
	Handle(*Request)
}

type AbstractHandler struct {
	next Handler
}

func (h *AbstractHandler) SetNext(next Handler) {
	h.next = next
}

type LowHandler struct {
	AbstractHandler
}

func (h *LowHandler) Handle(req *Request) {
	if req.level <= 1 {
		fmt.Printf("LowHandler: Processing %s\n", req.message)
	} else if h.next != nil {
		h.next.Handle(req)
	}
}

type MidHandler struct {
	AbstractHandler
}

func (h *MidHandler) Handle(req *Request) {
	if req.level == 2 {
		fmt.Printf("MidHandler: Processing %s\n", req.message)
	} else if h.next != nil {
		h.next.Handle(req)
	}
}

type HighHandler struct {
	AbstractHandler
}

func (h *HighHandler) Handle(req *Request) {
	if req.level >= 3 {
		fmt.Printf("HighHandler: Processing %s\n", req.message)
	}
}

func main() {
	low := &LowHandler{}
	mid := &MidHandler{}
	high := &HighHandler{}

	low.SetNext(mid)
	mid.SetNext(high)

	low.Handle(&Request{1, "Simple"})
	low.Handle(&Request{2, "Normal"})
	low.Handle(&Request{3, "Critical"})
}
