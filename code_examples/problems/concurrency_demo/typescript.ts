#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";

function partialSum(arr: number[]): Promise<number> {
  return new Promise((resolve) => {
    setImmediate(() => {
      resolve(arr.reduce((a, b) => a + b, 0));
    });
  });
}

async function main() {
  const n = 1000;
  const data = Array.from({ length: n }, (_, i) => i + 1);
  const workers = Math.min(8, Math.max(1, Math.floor(n / 100)));
  const chunk = Math.floor(n / workers);
  const chunks: number[][] = [];

  for (let i = 0; i < workers; i++) {
    const start = i * chunk;
    const end = i + 1 === workers ? n : (i + 1) * chunk;
    chunks.push(data.slice(start, end));
  }

  const results = await Promise.all(chunks.map((values) => partialSum(values)));
  console.log("Total:", results.reduce((a, b) => a + b, 0));
}

main().catch((err) => {
  console.error("Error:", err);
  process.exit(1);
});
