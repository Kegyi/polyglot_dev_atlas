function binaryToString(n: number): string {
  let result = "0.";
  while (n > 0) {
    if (result.length > 32) return "ERROR";
    n *= 2;
    if (n >= 1) {
      result += "1";
      n -= 1;
    } else {
      result += "0";
    }
  }
  return result;
}

console.log(binaryToString(0.625));
console.log(binaryToString(0.1));
