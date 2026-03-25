#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";
import { promises as fs } from "fs";

async function main(): Promise<void> {
  const path = "file_io_demo.txt";
  await fs.writeFile(path, "apple\nbanana\ncarrot\n", "utf8");

  const content = await fs.readFile(path, "utf8");
  const lines = content.trim().split(/\r?\n/);
  console.log("read lines:", lines);
}

main()
  .then(() => setImmediate(() => {}))
  .catch((err) => {
    console.error("error:", err);
    process.exit(1);
  });
