#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";

enum Status {
  Pending = "pending",
  Running = "running",
  Done = "done",
}

const MAX_RETRIES = 3;

function main(): void {
  const status = Status.Running;
  console.log("status:", status);
  console.log("max retries:", MAX_RETRIES);
}

main();
setImmediate(() => {});
