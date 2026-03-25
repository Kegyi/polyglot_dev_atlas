function topKFrequent(nums: number[], k: number): number[] {
  const freq = new Map<number, number>();
  for (const n of nums) {
    freq.set(n, (freq.get(n) ?? 0) + 1);
  }

  const pairs = Array.from(freq.entries()).map(([value, count]) => ({ value, count }));
  pairs.sort((a, b) => b.count - a.count);

  return pairs.slice(0, k).map((p) => p.value);
}

function main(): void {
  const nums = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 5, 5];
  const k = 2;
  const result = topKFrequent(nums, k);

  console.log("top k frequent:", ...result);
}

main();
