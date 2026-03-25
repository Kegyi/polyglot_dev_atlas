#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";

type User = {
  name: string;
  age: number;
};

function main(): void {
  const user: User = { name: "Alice", age: 29 };
  const text = JSON.stringify(user);
  const parsed = JSON.parse(text) as User;

  console.log("json:", text);
  console.log("parsed name:", parsed.name);
}

main();
setImmediate(() => {});
