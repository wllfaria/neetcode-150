from typing import Optional
from utils import flatten_list, make_list, ListNode


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


assert flatten_list(Solution().reverseList(make_list([0, 1, 2, 3]))) == [3, 2, 1, 0]
