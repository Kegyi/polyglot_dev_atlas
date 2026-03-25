function hasRoute(n: number, edges: Array<[number, number]>, start: number, target: number): boolean {
  const g: number[][] = Array.from({ length: n }, () => []);
  for (const [u, v] of edges) g[u].push(v);
  const seen = Array(n).fill(false);
  const q: number[] = [start];
  seen[start] = true;
  while (q.length) {
    const u = q.shift()!;
    if (u === target) return true;
    for (const v of g[u]) {
      if (!seen[v]) {
        seen[v] = true;
        q.push(v);
      }
    }
  }
  return false;
}

const edges: Array<[number, number]> = [[0, 1], [0, 2], [1, 3], [2, 4]];
console.log(hasRoute(5, edges, 0, 4));
console.log(hasRoute(5, edges, 3, 4));
