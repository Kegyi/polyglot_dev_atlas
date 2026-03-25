#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";

function main(): void {
  const values = [1, 2, 3, 4, 5];

  for (let i = 0; i < values.length; i++) {
    console.log("for index:", i, "->", values[i]);
  }

  for (const v of values) {
    if (v === 3) {
      continue;
    }
    console.log("for...of:", v);
  }

  let i = 0;
  while (i < values.length) {
    if (values[i] === 4) {
      break;
    }
    console.log("while:", values[i]);
    i++;
  }

  let c = 0;
  do {
    console.log("do...while iteration:", c);
    c++;
  } while (c < 2);
}

main();
setImmediate(() => {});
