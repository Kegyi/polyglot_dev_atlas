#!/usr/bin/env ts-node

interface Node {
  value: number;
  next: Node | null;
}

function makeNode(value: number, next: Node | null = null): Node {
  return { value, next };
}

function printList(head: Node | null): void {
  const parts: string[] = [];
  for (let cur = head; cur !== null; cur = cur.next) {
    parts.push(String(cur.value));
  }
  console.log(parts.join(" -> "));
}

function prepend(head: Node | null, value: number): Node {
  return makeNode(value, head);
}

function removeValue(head: Node | null, value: number): Node | null {
  if (head === null) return null;
  if (head.value === value) return head.next;
  head.next = removeValue(head.next, value);
  return head;
}

function main(): void {
  let head: Node | null = null;
  for (const v of [3, 2, 1]) head = prepend(head, v);  // 1 -> 2 -> 3
  printList(head);
  head = removeValue(head, 2);
  printList(head);  // 1 -> 3
}

main();
