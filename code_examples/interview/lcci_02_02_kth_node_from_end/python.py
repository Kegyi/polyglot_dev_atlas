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


def kth_to_last(head: ListNode, k: int) -> int:
    fast: ListNode | None = head
    slow: ListNode | None = head

    for _ in range(k):
        assert fast is not None
        fast = fast.next

    while fast is not None:
        fast = fast.next
        assert slow is not None
        slow = slow.next

    assert slow is not None
    return slow.val


def main() -> None:
    head = build_list([1, 2, 3, 4, 5])
    assert head is not None
    print(kth_to_last(head, 2))


if __name__ == "__main__":
    main()
