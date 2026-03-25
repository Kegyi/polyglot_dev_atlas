#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";

function parsePort(value: string): number {
  const parsed = Number(value);
  if (!Number.isFinite(parsed)) {
    throw new Error("invalid port");
  }
  return parsed;
}

function main(): void {
  try {
    const port = parsePort("not-a-number");
    console.log("port:", port);
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    console.log("parse failed:", message);
    console.log("fallback port:", 8080);
  }

  console.log("program continues");
}

main();
setImmediate(() => {});
