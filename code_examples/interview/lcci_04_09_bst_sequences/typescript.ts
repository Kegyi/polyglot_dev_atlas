class Node {
  constructor(
    public val: number,
    public left: Node | null = null,
    public right: Node | null = null
  ) {}
}

function weave(first: number[], second: number[], prefix: number[], out: number[][]): void {
  if (first.length === 0 || second.length === 0) {
    out.push([...prefix, ...first, ...second]);
    return;
  }

  weave(first.slice(1), second, [...prefix, first[0]], out);
  weave(first, second.slice(1), [...prefix, second[0]], out);
}

function allSeq(root: Node | null): number[][] {
  if (!root) return [[]];
  const left = allSeq(root.left);
  const right = allSeq(root.right);
  const result: number[][] = [];

  for (const l of left) {
    for (const r of right) {
      const weaved: number[][] = [];
      weave(l, r, [root.val], weaved);
      result.push(...weaved);
    }
  }
  return result;
}

const root = new Node(2, new Node(1), new Node(3));
for (const seq of allSeq(root)) {
  console.log(seq.join(" "));
}
