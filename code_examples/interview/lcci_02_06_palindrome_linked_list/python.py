class ListNode:
    def __init__(self, val: int, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def build_list(nums: list[int]) -> ListNode | None:
    dummy = ListNode(0)
    tail = dummy
    for n in nums:
        tail.next = ListNode(n)
        tail = tail.next
    return dummy.next


def reverse_list(head: ListNode | None) -> ListNode | None:
    prev = None
    while head is not None:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev


def is_palindrome(head: ListNode | None) -> bool:
    if head is None or head.next is None:
        return True

    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    second = reverse_list(slow)
    p1 = head
    p2 = second
    while p2 is not None:
        if p1 is None or p1.val != p2.val:
            return False
        p1 = p1.next
        p2 = p2.next
    return True


def main() -> None:
    a = build_list([1, 2, 2, 1])
    b = build_list([1, 2, 3, 2, 1])
    print(is_palindrome(a))
    print(is_palindrome(b))


if __name__ == "__main__":
    main()
