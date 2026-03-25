#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";

function main(): void {
  const values = [1, 2, 3, 4, 5];
  console.log("original:", values);

  const doubled = values.map((x) => x * 2);
  const evens = doubled.filter((x) => x % 2 === 0);
  const total = evens.reduce((sum, x) => sum + x, 0);

  console.log("doubled:", doubled);
  console.log("evens:", evens);
  console.log("sum of evens in doubled:", total);
}

main();
setImmediate(() => {});
