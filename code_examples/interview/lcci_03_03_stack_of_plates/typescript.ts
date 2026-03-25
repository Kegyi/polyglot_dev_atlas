class StackOfPlates {
  private readonly cap: number;
  private stacks: number[][] = [];

  constructor(capacity: number) {
    this.cap = capacity;
  }

  push(val: number): void {
    if (this.cap <= 0) {
      return;
    }
    if (this.stacks.length === 0 || this.stacks[this.stacks.length - 1].length === this.cap) {
      this.stacks.push([]);
    }
    this.stacks[this.stacks.length - 1].push(val);
  }

  pop(): number {
    return this.popAt(this.stacks.length - 1);
  }

  popAt(index: number): number {
    if (index < 0 || index >= this.stacks.length || this.stacks[index].length === 0) {
      return -1;
    }
    const val = this.stacks[index].pop()!;
    if (this.stacks[index].length === 0) {
      this.stacks.splice(index, 1);
    }
    return val;
  }
}

function main(): void {
  const s = new StackOfPlates(2);
  s.push(1);
  s.push(2);
  s.push(3);
  s.push(4);
  console.log(s.popAt(0));
  console.log(s.pop());
  console.log(s.pop());
  console.log(s.pop());
}

main();
