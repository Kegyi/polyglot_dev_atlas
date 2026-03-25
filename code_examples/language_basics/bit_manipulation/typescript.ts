#!/usr/bin/env ts-node

function countBits(n: number): number {
  let count = 0;
  while (n !== 0) {
    count += n & 1;
    n >>>= 1;
  }
  return count;
}

function main(): void {
  const a = 0b1010;  // 10
  const b = 0b1100;  // 12
  console.log("a & b: ", (a & b).toString(2).padStart(4, "0"));  // 1000
  console.log("a | b: ", (a | b).toString(2).padStart(4, "0"));  // 1110
  console.log("a ^ b: ", (a ^ b).toString(2).padStart(4, "0"));  // 0110

  let n = 0b0101;
  console.log("bit 1 set?", (n >> 1) & 1);  // check -> 0
  n |= (1 << 2);   // set bit 2
  n &= ~(1 << 0);  // clear bit 0
  console.log("after set/clear:", n.toString(2).padStart(4, "0"));  // 0100

  console.log("count bits in 7:", countBits(7));  // 3
}

main();
