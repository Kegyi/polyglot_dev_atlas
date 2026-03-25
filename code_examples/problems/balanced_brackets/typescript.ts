import { setImmediate } from "node:timers";

function isBalanced(s: string): boolean {
  const closeToOpen: Record<string, string> = {
    ")": "(",
    "]": "[",
    "}": "{",
  };

  const stack: string[] = [];
  for (const ch of s) {
    if (ch === "(" || ch === "[" || ch === "{") {
      stack.push(ch);
    } else if (ch in closeToOpen) {
      if (stack.length === 0 || stack[stack.length - 1] !== closeToOpen[ch]) {
        return false;
      }
      stack.pop();
    }
  }

  return stack.length === 0;
}

function main(): void {
  const input1 = "([{}])(()[]){}";
  const input2 = "([)]";

  console.log(`input_1 valid: ${isBalanced(input1)}`);
  console.log(`input_2 valid: ${isBalanced(input2)}`);
}

main();
setImmediate(() => {});
