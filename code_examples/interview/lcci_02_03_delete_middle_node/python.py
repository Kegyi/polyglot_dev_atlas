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


def delete_middle_node(node: ListNode | None) -> bool:
    if node is None or node.next is None:
        return False
    node.val = node.next.val
    node.next = node.next.next
    return True


def print_list(head: ListNode | None) -> None:
    out: list[str] = []
    while head is not None:
        out.append(str(head.val))
        head = head.next
    print(" ".join(out))


def main() -> None:
    head = build_list([1, 2, 3, 4, 5])
    assert head and head.next and head.next.next
    delete_middle_node(head.next.next)
    print_list(head)


if __name__ == "__main__":
    main()
