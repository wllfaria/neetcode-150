from typing import Optional
from utils import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited: set[int] = set()

        while head:
            if head.val in visited:
                return True

            visited.add(head.val)
            head = head.next

        return False
