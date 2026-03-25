#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";

function factorial(n: number): number {
  if (n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

function sumRecursive(values: number[], index = 0): number {
  if (index >= values.length) {
    return 0;
  }
  return values[index] + sumRecursive(values, index + 1);
}

function main(): void {
  const values = [1, 2, 3, 4];
  console.log("factorial(5):", factorial(5));
  console.log("sumRecursive(values):", sumRecursive(values));
}

main();
setImmediate(() => {});
