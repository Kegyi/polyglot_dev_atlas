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

function getIntersectionNode(a: ListNode | null, b: ListNode | null): ListNode | null {
  if (a === null || b === null) {
    return null;
  }

  let p1: ListNode | null = a;
  let p2: ListNode | null = b;
  while (p1 !== p2) {
    p1 = p1 !== null ? p1.next : b;
    p2 = p2 !== null ? p2.next : a;
  }
  return p1;
}

function main(): void {
  const common = buildList([8, 10]);
  const a = buildList([3, 1, 5, 9]);
  const b = buildList([4, 6]);

  let tailA = a;
  while (tailA !== null && tailA.next !== null) {
    tailA = tailA.next;
  }
  if (tailA !== null) {
    tailA.next = common;
  }

  let tailB = b;
  while (tailB !== null && tailB.next !== null) {
    tailB = tailB.next;
  }
  if (tailB !== null) {
    tailB.next = common;
  }

  const node = getIntersectionNode(a, b);
  console.log(node ? node.val : "null");
}

main();
