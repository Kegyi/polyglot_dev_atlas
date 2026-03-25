function flipBit(num: number): number {
  // Work with 32-bit unsigned
  num = num >>> 0;
  if (num === 0xffffffff) return 32;
  let cur = 0, prev = 0, best = 1;
  while (num > 0) {
    if (num & 1) {
      cur++;
    } else {
      prev = cur;
      cur = 0;
    }
    best = Math.max(best, prev + 1 + cur);
    num >>>= 1;
  }
  return best;
}

console.log(flipBit(1775));
console.log(flipBit(7));
