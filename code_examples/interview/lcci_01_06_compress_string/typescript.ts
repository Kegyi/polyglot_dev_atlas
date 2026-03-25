function compressString(s: string): string {
  if (s.length === 0) {
    return s;
  }

  let out = "";
  let run = 1;

  for (let i = 1; i <= s.length; i++) {
    if (i < s.length && s[i] === s[i - 1]) {
      run += 1;
      continue;
    }

    out += s[i - 1] + String(run);
    run = 1;
  }

  return out.length < s.length ? out : s;
}

function main(): void {
  console.log(`aabcccccaaa -> ${compressString("aabcccccaaa")}`);
  console.log(`abbccd -> ${compressString("abbccd")}`);
}

main();
