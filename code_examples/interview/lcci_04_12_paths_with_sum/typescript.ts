class Node {
  constructor(
    public val: number,
    public left: Node | null = null,
    public right: Node | null = null
  ) {}
}

function pathSum(root: Node | null, target: number): number {
  const count = new Map<number, number>();
  count.set(0, 1);

  const dfs = (node: Node | null, prefix: number): number => {
    if (!node) return 0;
    prefix += node.val;
    let res = count.get(prefix - target) ?? 0;
    count.set(prefix, (count.get(prefix) ?? 0) + 1);
    res += dfs(node.left, prefix);
    res += dfs(node.right, prefix);
    count.set(prefix, (count.get(prefix) ?? 1) - 1);
    return res;
  };

  return dfs(root, 0);
}

const root = new Node(
  10,
  new Node(5, new Node(3, new Node(3), new Node(-2)), new Node(2, null, new Node(1))),
  new Node(-3, null, new Node(11))
);
console.log(pathSum(root, 8));
