function checkPermutation(a: string, b: string): boolean {
  if (a.length !== b.length) {
    return false;
  }

  const freq = new Map<string, number>();
  for (const ch of a) {
    freq.set(ch, (freq.get(ch) ?? 0) + 1);
  }

  for (const ch of b) {
    const left = (freq.get(ch) ?? 0) - 1;
    if (left < 0) {
      return false;
    }
    freq.set(ch, left);
  }

  return true;
}

function main(): void {
  console.log(`abcde vs edcba -> ${checkPermutation("abcde", "edcba")}`);
  console.log(`abc vs abz -> ${checkPermutation("abc", "abz")}`);
}

main();
