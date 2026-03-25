#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";

function main(): void {
  const first = "hello";
  const second = "world";
  const joined = `${first} ${second}`;

  const part = joined.slice(0, 5);
  const replaced = joined.replace("hello", "hi");
  const words = joined.split(/\s+/);

  console.log("joined:", joined);
  console.log("part:", part);
  console.log("replaced:", replaced);
  console.log("tokens:", words);
}

main();
setImmediate(() => {});
