#!/usr/bin/env ts-node

interface TreeNode {
  value: number;
  left: TreeNode | null;
  right: TreeNode | null;
}

function makeNode(value: number): TreeNode {
  return { value, left: null, right: null };
}

function insert(root: TreeNode | null, value: number): TreeNode {
  if (root === null) return makeNode(value);
  if (value < root.value) root.left  = insert(root.left,  value);
  else                    root.right = insert(root.right, value);
  return root;
}

function inOrder(root: TreeNode | null): number[] {
  if (root === null) return [];
  return [...inOrder(root.left), root.value, ...inOrder(root.right)];
}

function bfs(root: TreeNode | null): number[] {
  if (root === null) return [];
  const result: number[] = [];
  const queue: TreeNode[] = [root];
  while (queue.length > 0) {
    const node = queue.shift()!;
    result.push(node.value);
    if (node.left)  queue.push(node.left);
    if (node.right) queue.push(node.right);
  }
  return result;
}

function main(): void {
  let root: TreeNode | null = null;
  for (const v of [5, 3, 7, 1, 4]) root = insert(root, v);
  console.log("in-order:", inOrder(root));  // [1, 3, 4, 5, 7]
  console.log("bfs:     ", bfs(root));      // [5, 3, 7, 1, 4]
}

main();
