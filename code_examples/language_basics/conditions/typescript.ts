#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";

function gradeToLabel(grade: number): string {
  if (grade >= 90) return "excellent";
  if (grade >= 75) return "good";
  if (grade >= 60) return "pass";
  return "fail";
}

function main(): void {
  const grade = 82;
  const code = 2;

  console.log("if/else:", gradeToLabel(grade));

  switch (code) {
    case 1:
      console.log("switch: created");
      break;
    case 2:
      console.log("switch: updated");
      break;
    case 3:
      console.log("switch: deleted");
      break;
    default:
      console.log("switch: unknown");
  }

  const ready = grade >= 60;
  console.log("ternary:", ready ? "can continue" : "needs retry");
}

main();
setImmediate(() => {});
