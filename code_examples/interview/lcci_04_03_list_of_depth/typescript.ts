class Node {
  constructor(
    public val: number,
    public left: Node | null = null,
    public right: Node | null = null
  ) {}
}

function listOfDepth(root: Node | null): number[][] {
  if (!root) return [];
  const out: number[][] = [];
  const q: Node[] = [root];
  while (q.length) {
    const n = q.length;
    const level: number[] = [];
    for (let i = 0; i < n; i++) {
      const cur = q.shift()!;
      level.push(cur.val);
      if (cur.left) q.push(cur.left);
      if (cur.right) q.push(cur.right);
    }
    out.push(level);
  }
  return out;
}

const root = new Node(1, new Node(2, new Node(4), new Node(5)), new Node(3, new Node(6), new Node(7)));
console.log(listOfDepth(root).map((lvl) => lvl.join(" ")).join(" | "));
