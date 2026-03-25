class Node {
  constructor(
    public val: number,
    public left: Node | null = null,
    public right: Node | null = null
  ) {}
}

function same(a: Node | null, b: Node | null): boolean {
  if (!a && !b) return true;
  if (!a || !b) return false;
  return a.val === b.val && same(a.left, b.left) && same(a.right, b.right);
}

function isSubtree(t1: Node | null, t2: Node | null): boolean {
  if (!t2) return true;
  if (!t1) return false;
  if (same(t1, t2)) return true;
  return isSubtree(t1.left, t2) || isSubtree(t1.right, t2);
}

const t1 = new Node(3, new Node(4, new Node(1), new Node(2)), new Node(5));
const t2 = new Node(4, new Node(1), new Node(2));
const t3 = new Node(4, new Node(1), new Node(3));

console.log(isSubtree(t1, t2));
console.log(isSubtree(t1, t3));
