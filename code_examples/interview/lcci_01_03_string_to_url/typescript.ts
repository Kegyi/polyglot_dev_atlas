function urlify(s: string, trueLength: number): string {
  let out = "";
  for (let i = 0; i < trueLength; i++) {
    out += s[i] === " " ? "%20" : s[i];
  }
  return out;
}

function main(): void {
  console.log(urlify("Mr John Smith    ", 13));
}

main();
