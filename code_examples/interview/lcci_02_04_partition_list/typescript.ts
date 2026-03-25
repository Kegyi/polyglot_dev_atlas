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

function partition(head: ListNode | null, x: number): ListNode | null {
  const lessDummy = new ListNode(0);
  const greaterDummy = new ListNode(0);
  let lessTail = lessDummy;
  let greaterTail = greaterDummy;

  while (head !== null) {
    if (head.val < x) {
      lessTail.next = head;
      lessTail = lessTail.next;
    } else {
      greaterTail.next = head;
      greaterTail = greaterTail.next;
    }
    head = head.next;
  }

  greaterTail.next = null;
  lessTail.next = greaterDummy.next;
  return lessDummy.next;
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
  const head = buildList([3, 5, 8, 5, 10, 2, 1]);
  printList(partition(head, 5));
}

main();
