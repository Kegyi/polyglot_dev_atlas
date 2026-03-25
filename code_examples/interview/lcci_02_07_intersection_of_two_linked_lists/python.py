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


def get_intersection_node(a: ListNode | None, b: ListNode | None) -> ListNode | None:
    if a is None or b is None:
        return None

    p1, p2 = a, b
    while p1 is not p2:
        p1 = p1.next if p1 is not None else b
        p2 = p2.next if p2 is not None else a
    return p1


def main() -> None:
    common = build_list([8, 10])

    a = build_list([3, 1, 5, 9])
    b = build_list([4, 6])

    tail_a = a
    while tail_a is not None and tail_a.next is not None:
        tail_a = tail_a.next
    if tail_a is not None:
        tail_a.next = common

    tail_b = b
    while tail_b is not None and tail_b.next is not None:
        tail_b = tail_b.next
    if tail_b is not None:
        tail_b.next = common

    node = get_intersection_node(a, b)
    print(node.val if node else "null")


if __name__ == "__main__":
    main()
