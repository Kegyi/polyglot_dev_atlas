#!/usr/bin/env ts-node

class MinHeap {
  private data: number[] = [];

  push(v: number): void {
    this.data.push(v);
    this.bubbleUp(this.data.length - 1);
  }

  pop(): number {
    const top = this.data[0];
    const last = this.data.pop()!;
    if (this.data.length > 0) { this.data[0] = last; this.sinkDown(0); }
    return top;
  }

  peek(): number { return this.data[0]; }
  size(): number { return this.data.length; }

  private bubbleUp(i: number): void {
    while (i > 0) {
      const parent = (i - 1) >> 1;
      if (this.data[parent] <= this.data[i]) break;
      [this.data[parent], this.data[i]] = [this.data[i], this.data[parent]];
      i = parent;
    }
  }

  private sinkDown(i: number): void {
    const n = this.data.length;
    while (true) {
      let min = i;
      const l = 2 * i + 1, r = 2 * i + 2;
      if (l < n && this.data[l] < this.data[min]) min = l;
      if (r < n && this.data[r] < this.data[min]) min = r;
      if (min === i) break;
      [this.data[min], this.data[i]] = [this.data[i], this.data[min]];
      i = min;
    }
  }
}

function main(): void {
  const data = [3, 1, 4, 1, 5, 9];

  // min-heap
  const minHeap = new MinHeap();
  for (const v of data) minHeap.push(v);
  console.log("min:", minHeap.peek());  // 1
  const drained: number[] = [];
  while (minHeap.size() > 0) drained.push(minHeap.pop());
  console.log("drain min-heap:", drained);  // [1,1,3,4,5,9]

  // max-heap via negation
  const maxHeap = new MinHeap();
  for (const v of data) maxHeap.push(-v);
  console.log("max:", -maxHeap.peek());  // 9
}

main();
