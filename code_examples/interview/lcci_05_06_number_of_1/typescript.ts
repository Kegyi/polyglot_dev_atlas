function convertInteger(A: number, B: number): number {
  let x = (A ^ B) >>> 0;
  let count = 0;
  while (x) {
    count += x & 1;
    x >>>= 1;
  }
  return count;
}

console.log(convertInteger(29, 15));
console.log(convertInteger(1, 5));
