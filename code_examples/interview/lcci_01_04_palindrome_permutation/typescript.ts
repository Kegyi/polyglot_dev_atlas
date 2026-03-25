function canPermutePalindrome(s: string): boolean {
  const freq = new Map<string, number>();
  for (const ch of s.toLowerCase()) {
    if (ch === " ") {
      continue;
    }
    freq.set(ch, (freq.get(ch) ?? 0) + 1);
  }

  let odd = 0;
  for (const count of freq.values()) {
    if (count % 2 === 1) {
      odd += 1;
      if (odd > 1) {
        return false;
      }
    }
  }
  return true;
}

function main(): void {
  console.log(`tact coa -> ${canPermutePalindrome("tact coa")}`);
  console.log(`daily -> ${canPermutePalindrome("daily")}`);
}

main();
