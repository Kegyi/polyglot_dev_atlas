function insert(N: number, M: number, i: number, j: number): number {
  const mask = ~(((1 << (j - i + 1)) - 1) << i);
  return (N & mask) | (M << i);
}

console.log(insert(1024, 19, 2, 6));
console.log(insert(0, 19, 0, 4));
