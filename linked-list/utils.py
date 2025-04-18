from typing import Optional, Self


class ListNode:
    def __init__(self, val: int = 0, next: Optional[Self] = None):
        self.val = val
        self.next = next


def make_list(values: list[int]) -> ListNode | None:
    dummy = ListNode(-1)
    curr = dummy

    for v in values:
        curr.next = ListNode(v)
        curr = curr.next

    return dummy.next


def flatten_list(linked_list: Optional[ListNode]) -> list[int]:
    values: list[int] = []
    curr = linked_list

    while curr:
        values.append(curr.val)
        curr = curr.next

    return values
