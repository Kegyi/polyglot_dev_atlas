class Node {
  constructor(
    public val: number,
    public left: Node | null = null,
    public right: Node | null = null
  ) {}
}

function isValid(n: Node | null, lo: number, hi: number): boolean {
  if (!n) return true;
  if (!(lo < n.val && n.val < hi)) return false;
  return isValid(n.left, lo, n.val) && isValid(n.right, n.val, hi);
}

const ok = new Node(5, new Node(3), new Node(7));
const bad = new Node(5, new Node(3, null, new Node(6)), new Node(7));
console.log(isValid(ok, Number.NEGATIVE_INFINITY, Number.POSITIVE_INFINITY));
console.log(isValid(bad, Number.NEGATIVE_INFINITY, Number.POSITIVE_INFINITY));
