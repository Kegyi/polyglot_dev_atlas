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

function hasCycle(head: ListNode | null): boolean {
  let slow: ListNode | null = head;
  let fast: ListNode | null = head;
  while (fast !== null && fast.next !== null) {
    slow = slow!.next;
    fast = fast.next.next;
    if (slow === fast) {
      return true;
    }
  }
  return false;
}

function main(): void {
  const a = buildList([1, 2, 3, 4]);
  let tail = a;
  while (tail !== null && tail.next !== null) {
    tail = tail.next;
  }
  if (tail !== null && a !== null && a.next !== null) {
    tail.next = a.next;
  }

  const b = buildList([1, 2, 3, 4]);

  console.log(hasCycle(a));
  console.log(hasCycle(b));
}

main();
