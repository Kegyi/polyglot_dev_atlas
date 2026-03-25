function oneAway(a: string, b: string): boolean {
  if (Math.abs(a.length - b.length) > 1) {
    return false;
  }

  let s1 = a;
  let s2 = b;
  if (s1.length > s2.length) {
    [s1, s2] = [s2, s1];
  }

  let i = 0;
  let j = 0;
  let found = false;

  while (i < s1.length && j < s2.length) {
    if (s1[i] === s2[j]) {
      i += 1;
      j += 1;
      continue;
    }

    if (found) {
      return false;
    }
    found = true;

    if (s1.length === s2.length) {
      i += 1;
    }
    j += 1;
  }

  return true;
}

function main(): void {
  console.log(`pale vs ple -> ${oneAway("pale", "ple")}`);
  console.log(`pales vs pale -> ${oneAway("pales", "pale")}`);
  console.log(`pale vs bake -> ${oneAway("pale", "bake")}`);
}

main();
