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


def remove_duplicate_nodes(head: ListNode | None) -> None:
    seen: set[int] = set()
    prev: ListNode | None = None
    cur = head

    while cur is not None:
        if cur.val in seen:
            assert prev is not None
            prev.next = cur.next
            cur = cur.next
            continue
        seen.add(cur.val)
        prev = cur
        cur = cur.next


def print_list(head: ListNode | None) -> None:
    out: list[str] = []
    while head is not None:
        out.append(str(head.val))
        head = head.next
    print(" ".join(out))


def main() -> None:
    head = build_list([1, 2, 3, 3, 2, 1, 4])
    remove_duplicate_nodes(head)
    print_list(head)


if __name__ == "__main__":
    main()
