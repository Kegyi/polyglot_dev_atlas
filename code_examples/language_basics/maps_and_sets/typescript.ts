#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";

function main(): void {
  const counts = new Map<string, number>([
    ["apple", 2],
    ["banana", 1],
  ]);
  counts.set("apple", (counts.get("apple") ?? 0) + 3);

  const tags = new Set<string>(["fruit", "food"]);
  tags.add("fresh");

  console.log("apple count:", counts.get("apple"));
  console.log("all map entries:", Array.from(counts.entries()));
  console.log("all set entries:", Array.from(tags.values()));
}

main();
setImmediate(() => {});
