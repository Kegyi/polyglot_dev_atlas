#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";
import { mkdirSync, existsSync } from "fs";
import path from "path";

function main(): void {
  const base = "demo_folder";
  const filePath = path.join(base, "sub", "data.txt");
  const parent = path.dirname(filePath);

  mkdirSync(parent, { recursive: true });

  console.log("file path:", filePath);
  console.log("parent path:", parent);
  console.log("directory exists:", existsSync(parent));
}

main();
setImmediate(() => {});
