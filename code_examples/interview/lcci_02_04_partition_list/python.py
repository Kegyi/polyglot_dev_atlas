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


def partition(head: ListNode | None, x: int) -> ListNode | None:
    less_dummy = ListNode(0)
    greater_dummy = ListNode(0)
    less_tail = less_dummy
    greater_tail = greater_dummy

    while head is not None:
        if head.val < x:
            less_tail.next = head
            less_tail = less_tail.next
        else:
            greater_tail.next = head
            greater_tail = greater_tail.next
        head = head.next

    greater_tail.next = None
    less_tail.next = greater_dummy.next
    return less_dummy.next


def print_list(head: ListNode | None) -> None:
    out: list[str] = []
    while head is not None:
        out.append(str(head.val))
        head = head.next
    print(" ".join(out))


def main() -> None:
    head = build_list([3, 5, 8, 5, 10, 2, 1])
    print_list(partition(head, 5))


if __name__ == "__main__":
    main()
