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

function reverseList(head: ListNode | null): ListNode | null {
  let prev: ListNode | null = null;
  while (head !== null) {
    const nextNode = head.next;
    head.next = prev;
    prev = head;
    head = nextNode;
  }
  return prev;
}

function isPalindrome(head: ListNode | null): boolean {
  if (head === null || head.next === null) {
    return true;
  }

  let slow: ListNode | null = head;
  let fast: ListNode | null = head;
  while (fast !== null && fast.next !== null) {
    slow = slow!.next;
    fast = fast.next.next;
  }

  let p1: ListNode | null = head;
  let p2: ListNode | null = reverseList(slow);
  while (p2 !== null) {
    if (p1 === null || p1.val !== p2.val) {
      return false;
    }
    p1 = p1.next;
    p2 = p2.next;
  }
  return true;
}

function main(): void {
  const a = buildList([1, 2, 2, 1]);
  const b = buildList([1, 2, 3, 2, 1]);
  console.log(isPalindrome(a));
  console.log(isPalindrome(b));
}

main();
