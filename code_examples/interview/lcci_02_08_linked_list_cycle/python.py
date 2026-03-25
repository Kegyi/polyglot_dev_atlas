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


def has_cycle(head: ListNode | None) -> bool:
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next if slow is not None else None
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def main() -> None:
    a = build_list([1, 2, 3, 4])
    tail = a
    while tail is not None and tail.next is not None:
        tail = tail.next
    if tail is not None and a is not None and a.next is not None:
        tail.next = a.next

    b = build_list([1, 2, 3, 4])

    print(has_cycle(a))
    print(has_cycle(b))


if __name__ == "__main__":
    main()
