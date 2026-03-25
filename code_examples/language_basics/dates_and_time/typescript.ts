#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";

function main(): void {
  const now = new Date();
  const later = new Date(now.getTime() + 90 * 60 * 1000);

  console.log("now:", now.toISOString());
  console.log("later:", later.toISOString());
  console.log("later > now:", later > now);
}

main();
setImmediate(() => {});
