#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";

function parseAge(text: string): number | null {
  if (text === "") {
    return null;
  }
  return Number(text);
}

function main(): void {
  const age = parseAge("29");
  const missing = parseAge("");

  console.log("age present:", age !== null);
  console.log("missing default:", missing ?? 0);
}

main();
setImmediate(() => {});
