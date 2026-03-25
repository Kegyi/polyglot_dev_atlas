function findClosedNumbers(num: number): [number, number] {
  let bigger = num, smaller = num;

  for (let i = 1; i < 32; i++) {
    if ((bigger >> (i - 1)) & 1 && !((bigger >> i) & 1)) {
      bigger |= 1 << i;
      bigger &= ~(1 << (i - 1));
      break;
    }
  }

  for (let i = 1; i < 32; i++) {
    if (!((smaller >> (i - 1)) & 1) && (smaller >> i) & 1) {
      smaller &= ~(1 << i);
      smaller |= 1 << (i - 1);
      break;
    }
  }

  return [bigger, smaller];
}

const [bigger, smaller] = findClosedNumbers(2);
console.log(bigger);
console.log(smaller);
