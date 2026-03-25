function exchangeBits(num: number): number {
  const u = num >>> 0;
  return (((u & 0xAAAAAAAA) >>> 1) | ((u & 0x55555555) << 1)) >>> 0;
}

console.log(exchangeBits(2));
console.log(exchangeBits(3));
