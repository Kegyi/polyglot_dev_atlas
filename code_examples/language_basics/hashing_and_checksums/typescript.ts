#!/usr/bin/env ts-node

import { createHash } from "node:crypto";
import { setImmediate } from "node:timers";

function checksum(text: string): number {
  return Array.from(text).reduce((acc, ch) => acc + ch.charCodeAt(0), 0);
}

function main(): void {
  const text = "hello-world";
  const sha256Hex = createHash("sha256").update(text).digest("hex");
  const sum = checksum(text);

  console.log("text:", text);
  console.log("sha256:", sha256Hex);
  console.log("checksum:", sum);
}

main();
setImmediate(() => {});
