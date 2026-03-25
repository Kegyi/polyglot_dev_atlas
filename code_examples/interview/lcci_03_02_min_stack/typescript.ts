class MinStack {
  private readonly values: number[] = [];
  private readonly mins: number[] = [];

  push(x: number): void {
    this.values.push(x);
    if (this.mins.length === 0 || x <= this.mins[this.mins.length - 1]) {
      this.mins.push(x);
    }
  }

  pop(): void {
    if (this.values.length === 0) {
      return;
    }
    const top = this.values.pop()!;
    if (top === this.mins[this.mins.length - 1]) {
      this.mins.pop();
    }
  }

  top(): number {
    return this.values.length ? this.values[this.values.length - 1] : -1;
  }

  getMin(): number {
    return this.mins.length ? this.mins[this.mins.length - 1] : -1;
  }
}

function main(): void {
  const st = new MinStack();
  st.push(3);
  st.push(5);
  st.push(2);
  st.push(2);
  console.log(st.getMin());
  st.pop();
  console.log(st.getMin());
  st.pop();
  console.log(st.getMin());
}

main();
