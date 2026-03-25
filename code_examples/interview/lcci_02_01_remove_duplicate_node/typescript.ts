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

function removeDuplicateNodes(head: ListNode | null): void {
  const seen = new Set<number>();
  let prev: ListNode | null = null;
  let cur = head;

  while (cur !== null) {
    if (seen.has(cur.val)) {
      if (prev !== null) {
        prev.next = cur.next;
      }
      cur = cur.next;
      continue;
    }

    seen.add(cur.val);
    prev = cur;
    cur = cur.next;
  }
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
  const head = buildList([1, 2, 3, 3, 2, 1, 4]);
  removeDuplicateNodes(head);
  printList(head);
}

main();
