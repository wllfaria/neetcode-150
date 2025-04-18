from typing import Optional, Self


class ListNode:
    def __init__(self, val: int = 0, next: Optional[Self] = None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev


def make_list(values: list[int]) -> ListNode | None:
    dummy = ListNode(-1)
    curr = dummy

    for v in values:
        curr.next = ListNode(v)
        curr = curr.next

    return dummy.next


print(Solution().reverseList(make_list([0, 1, 2, 3])))
