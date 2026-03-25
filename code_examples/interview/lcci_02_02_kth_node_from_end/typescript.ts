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

function kthToLast(head: ListNode, k: number): number {
  let fast: ListNode | null = head;
  let slow: ListNode | null = head;

  for (let i = 0; i < k; i++) {
    fast = fast!.next;
  }

  while (fast !== null) {
    fast = fast.next;
    slow = slow!.next;
  }

  return slow!.val;
}

function main(): void {
  const head = buildList([1, 2, 3, 4, 5])!;
  console.log(kthToLast(head, 2));
}

main();
