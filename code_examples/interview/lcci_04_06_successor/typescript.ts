class Node {
  constructor(
    public val: number,
    public left: Node | null = null,
    public right: Node | null = null
  ) {}
}

function inorderSuccessor(root: Node | null, p: number): Node | null {
  let ans: Node | null = null;
  while (root) {
    if (p < root.val) {
      ans = root;
      root = root.left;
    } else {
      root = root.right;
    }
  }
  return ans;
}

const root = new Node(5, new Node(3, new Node(2), new Node(4)), new Node(7));
console.log(inorderSuccessor(root, 3)?.val ?? -1);
console.log(inorderSuccessor(root, 7)?.val ?? -1);
