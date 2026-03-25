class Node {
  constructor(
    public val: number,
    public left: Node | null = null,
    public right: Node | null = null
  ) {}
}

function lca(root: Node | null, p: number, q: number): Node | null {
  if (!root || root.val === p || root.val === q) return root;
  const left = lca(root.left, p, q);
  const right = lca(root.right, p, q);
  if (left && right) return root;
  return left ?? right;
}

const root = new Node(
  3,
  new Node(5, new Node(6), new Node(2)),
  new Node(1, new Node(0), new Node(8))
);

console.log(lca(root, 6, 2)?.val ?? -1);
console.log(lca(root, 6, 8)?.val ?? -1);
