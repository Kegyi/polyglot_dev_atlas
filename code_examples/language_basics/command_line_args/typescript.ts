#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";

function main(): void {
  const args = process.argv.slice(2);
  const name = args[0] ?? "world";
  const excited = args.includes("--excited");

  let message = `Hello, ${name}`;
  if (excited) {
    message += "!";
  }

  console.log(message);
}

main();
setImmediate(() => {});
