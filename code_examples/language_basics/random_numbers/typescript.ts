#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";

function makeGenerator(seed: number): () => number {
  let state = seed;
  return () => {
    state = (state * 1664525 + 1013904223) % 4294967296;
    return state / 4294967296;
  };
}

function main(): void {
  const next = makeGenerator(42);
  const draws = Array.from({ length: 3 }, () => Math.floor(next() * 10) + 1);
  console.log("draws:", draws);
}

main();
setImmediate(() => {});
