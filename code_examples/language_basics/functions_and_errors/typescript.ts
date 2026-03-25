#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";

function add(a: number, b: number): number {
  return a + b;
}

function safeDiv(a: number, b: number): number | null {
  if (b === 0) return null;
  return a / b;
}

function strictDiv(a: number, b: number): number {
  if (b === 0) throw new Error("division by zero");
  return a / b;
}

function main(): void {
  console.log("add(2, 3):", add(2, 3));
  console.log("safeDiv(10, 2):", safeDiv(10, 2));

  try {
    console.log("strictDiv(10, 0):", strictDiv(10, 0));
  } catch (err) {
    console.error("error:", err);
  }
}

main();
setImmediate(() => {});
