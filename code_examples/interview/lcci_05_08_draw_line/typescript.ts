function drawLine(
  length: number,
  w: number,
  x1: number,
  x2: number,
  y: number
): number[] {
  const wordsPerRow = (w / 32) | 0;
  const screen = new Array<number>(length).fill(0);
  const offset = y * wordsPerRow;

  const startWord = ((x1 / 32) | 0) + offset;
  const endWord = ((x2 / 32) | 0) + offset;
  const startBit = x1 % 32;
  const endBit = x2 % 32;

  for (let i = startWord; i <= endWord; i++) {
    let hi = i === startWord ? 0xff >> startBit : 0xff;
    let lo = i === endWord ? ~(0xff >> (endBit + 1)) & 0xff : 0xff;
    screen[i] = hi & lo;
  }
  return screen;
}

const result = drawLine(1, 32, 1, 30, 0);
for (const v of result) console.log(v.toString(16));
