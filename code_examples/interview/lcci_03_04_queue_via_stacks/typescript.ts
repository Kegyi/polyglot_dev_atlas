class MyQueue {
  private readonly inStack: number[] = [];
  private readonly outStack: number[] = [];

  push(x: number): void {
    this.inStack.push(x);
  }

  private moveIfNeeded(): void {
    if (this.outStack.length) {
      return;
    }
    while (this.inStack.length) {
      this.outStack.push(this.inStack.pop()!);
    }
  }

  pop(): number {
    this.moveIfNeeded();
    return this.outStack.length ? this.outStack.pop()! : -1;
  }

  peek(): number {
    this.moveIfNeeded();
    return this.outStack.length ? this.outStack[this.outStack.length - 1] : -1;
  }

  empty(): boolean {
    return this.inStack.length === 0 && this.outStack.length === 0;
  }
}

function main(): void {
  const q = new MyQueue();
  q.push(1);
  q.push(2);
  q.push(3);
  console.log(q.peek());
  console.log(q.pop());
  console.log(q.pop());
  console.log(q.empty());
}

main();
