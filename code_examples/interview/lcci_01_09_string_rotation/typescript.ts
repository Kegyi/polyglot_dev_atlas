function isStringRotation(s1: string, s2: string): boolean {
  return s1.length === s2.length && (s1 + s1).includes(s2);
}

function main(): void {
  console.log(`waterbottle vs erbottlewat -> ${isStringRotation("waterbottle", "erbottlewat")}`);
  console.log(`aa vs aba -> ${isStringRotation("aa", "aba")}`);
}

main();
