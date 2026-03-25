#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";

function main(): void {
  const mode = process.env.APP_MODE ?? "development";
  const port = process.env.APP_PORT ?? "8080";

  console.log("mode:", mode);
  console.log("port:", port);
  console.log("has APP_MODE:", process.env.APP_MODE !== undefined);
}

main();
setImmediate(() => {});
