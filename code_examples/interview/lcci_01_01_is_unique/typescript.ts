function isUnique(s: string): boolean {
  const seen = new Set<string>();
  for (const ch of s) {
    if (seen.has(ch)) {
      return false;
    }
    seen.add(ch);
  }
  return true;
}

function main(): void {
  console.log(`leetcode -> ${isUnique("leetcode")}`);
  console.log(`abc -> ${isUnique("abc")}`);
}

main();
