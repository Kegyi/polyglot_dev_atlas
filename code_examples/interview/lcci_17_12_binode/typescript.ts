class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;

    constructor(val = 0, left: TreeNode | null = null, right: TreeNode | null = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

function convertBiNode(root: TreeNode | null): TreeNode | null {
    const dummy = new TreeNode(0);
    let prev = dummy;

    const inorder = (node: TreeNode | null): void => {
        if (!node) return;
        inorder(node.left);
        node.left = null;
        prev.right = node;
        prev = node;
        inorder(node.right);
    };

    inorder(root);
    return dummy.right;
}

const root = new TreeNode(4);
root.left = new TreeNode(2);
root.right = new TreeNode(5);
root.left.left = new TreeNode(1);
root.left.right = new TreeNode(3);
root.right.right = new TreeNode(6);
root.left.left.left = new TreeNode(0);

let head = convertBiNode(root);
const out: number[] = [];
while (head) {
    out.push(head.val);
    head = head.right;
}
console.log(out.join(' ')); // 0 1 2 3 4 5 6
