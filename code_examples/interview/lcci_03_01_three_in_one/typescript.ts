class TripleInOne {
  private readonly size: number;
  private readonly data: number[];
  private readonly tops: number[];

  constructor(stackSize: number) {
    this.size = stackSize;
    this.data = new Array(3 * stackSize).fill(0);
    this.tops = [0, 0, 0];
  }

  push(stackNum: number, value: number): void {
    if (this.tops[stackNum] === this.size) {
      return;
    }
    const index = stackNum * this.size + this.tops[stackNum];
    this.data[index] = value;
    this.tops[stackNum] += 1;
  }

  pop(stackNum: number): number {
    if (this.tops[stackNum] === 0) {
      return -1;
    }
    this.tops[stackNum] -= 1;
    const index = stackNum * this.size + this.tops[stackNum];
    return this.data[index];
  }

  peek(stackNum: number): number {
    if (this.tops[stackNum] === 0) {
      return -1;
    }
    const index = stackNum * this.size + this.tops[stackNum] - 1;
    return this.data[index];
  }

  isEmpty(stackNum: number): boolean {
    return this.tops[stackNum] === 0;
  }
}

function main(): void {
  const stacks = new TripleInOne(2);
  stacks.push(0, 10);
  stacks.push(0, 11);
  stacks.push(0, 12);
  stacks.push(1, 20);
  console.log(stacks.peek(0));
  console.log(stacks.pop(0));
  console.log(stacks.pop(0));
  console.log(stacks.pop(0));
  console.log(stacks.isEmpty(1));
}

main();
