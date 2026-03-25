package main

import (
	"container/list"
	"fmt"
)

type node struct {
	key int
	val int
}

type LRUCache struct {
	cap  int
	list *list.List
	pos  map[int]*list.Element
}

func Constructor(capacity int) LRUCache {
	return LRUCache{cap: capacity, list: list.New(), pos: map[int]*list.Element{}}
}

func (c *LRUCache) Get(key int) int {
	if e, ok := c.pos[key]; ok {
		c.list.MoveToFront(e)
		return e.Value.(node).val
	}
	return -1
}

func (c *LRUCache) Put(key int, value int) {
	if e, ok := c.pos[key]; ok {
		e.Value = node{key: key, val: value}
		c.list.MoveToFront(e)
		return
	}
	if c.list.Len() == c.cap {
		tail := c.list.Back()
		delete(c.pos, tail.Value.(node).key)
		c.list.Remove(tail)
	}
	e := c.list.PushFront(node{key: key, val: value})
	c.pos[key] = e
}

func main() {
	cache := Constructor(2)
	cache.Put(1, 1)
	cache.Put(2, 2)
	fmt.Println(cache.Get(1))
	cache.Put(3, 3)
	fmt.Println(cache.Get(2))
	cache.Put(4, 4)
	fmt.Println(cache.Get(1))
	fmt.Println(cache.Get(3))
	fmt.Println(cache.Get(4))
}
