class ListNode {
  val: number;
  next: ListNode | null;

  constructor(val: number, next: ListNode | null = null) {
    this.val = val;
    this.next = next;
  }
}

function buildList(nums: number[]): ListNode | null {
  const dummy = new ListNode(0);
  let tail = dummy;
  for (const n of nums) {
    tail.next = new ListNode(n);
    tail = tail.next;
  }
  return dummy.next;
}

function deleteMiddleNode(node: ListNode | null): boolean {
  if (node === null || node.next === null) {
    return false;
  }
  node.val = node.next.val;
  node.next = node.next.next;
  return true;
}

function printList(head: ListNode | null): void {
  const out: number[] = [];
  while (head !== null) {
    out.push(head.val);
    head = head.next;
  }
  console.log(out.join(" "));
}

function main(): void {
  const head = buildList([1, 2, 3, 4, 5])!;
  deleteMiddleNode(head.next!.next!);
  printList(head);
}

main();
