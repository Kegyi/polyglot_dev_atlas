#!/usr/bin/env ts-node

class Stack<T> {
  private items: T[] = [];
  push(v: T): void { this.items.push(v); }
  pop(): void { this.items.pop(); }
  top(): T { return this.items[this.items.length - 1]; }
  isEmpty(): boolean { return this.items.length === 0; }
}

class Queue<T> {
  private items: T[] = [];
  enqueue(v: T): void { this.items.push(v); }
  dequeue(): void { this.items.shift(); }
  front(): T { return this.items[0]; }
  isEmpty(): boolean { return this.items.length === 0; }
}

function main(): void {
  const stk = new Stack<number>();
  for (const v of [1, 2, 3]) stk.push(v);
  console.log("stack top:", stk.top());  // 3 (LIFO)
  stk.pop();
  console.log("after pop:", stk.top());  // 2

  const q = new Queue<number>();
  for (const v of [1, 2, 3]) q.enqueue(v);
  console.log("queue front:", q.front());  // 1 (FIFO)
  q.dequeue();
  console.log("after dequeue:", q.front());  // 2
}

main();
