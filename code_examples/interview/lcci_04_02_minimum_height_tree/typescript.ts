class Node {
  constructor(
    public val: number,
    public left: Node | null = null,
    public right: Node | null = null
  ) {}
}

function build(a: number[], lo: number, hi: number): Node | null {
  if (lo > hi) return null;
  const mid = Math.floor((lo + hi) / 2);
  return new Node(a[mid], build(a, lo, mid - 1), build(a, mid + 1, hi));
}

function inorder(n: Node | null, out: number[]): void {
  if (!n) return;
  inorder(n.left, out);
  out.push(n.val);
  inorder(n.right, out);
}

const nums = [1, 2, 3, 4, 5, 6, 7];
const root = build(nums, 0, nums.length - 1);
const out: number[] = [];
inorder(root, out);
console.log(out.join(" "));
