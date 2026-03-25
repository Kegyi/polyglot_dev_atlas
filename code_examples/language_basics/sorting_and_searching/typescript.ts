#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";

function binarySearch(values: number[], target: number): number {
  let left = 0;
  let right = values.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    if (values[mid] === target) {
      return mid;
    }
    if (values[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return -1;
}

function main(): void {
  const values = [9, 3, 7, 1, 5].sort((a, b) => a - b);
  const index = binarySearch(values, 7);

  console.log("sorted:", values);
  console.log("contains 7:", index >= 0);
  console.log("index of 7:", index);
}

main();
setImmediate(() => {});
