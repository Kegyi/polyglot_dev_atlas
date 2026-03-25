class Node {
  constructor(
    public val: number,
    public left: Node | null = null,
    public right: Node | null = null
  ) {}
}

function heightOrFail(n: Node | null): number {
  if (!n) return 0;
  const lh = heightOrFail(n.left);
  if (lh === -1) return -1;
  const rh = heightOrFail(n.right);
  if (rh === -1) return -1;
  if (Math.abs(lh - rh) > 1) return -1;
  return 1 + Math.max(lh, rh);
}

function isBalanced(root: Node | null): boolean {
  return heightOrFail(root) !== -1;
}

const a = new Node(1, new Node(2), new Node(3));
const b = new Node(1, new Node(2, new Node(3, new Node(4))));
console.log(isBalanced(a));
console.log(isBalanced(b));
