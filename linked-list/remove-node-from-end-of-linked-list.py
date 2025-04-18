from typing import Optional
from utils import ListNode, flatten_list, make_list


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            # pylint is annoying here
            assert right
            right = right.next
            n -= 1

        while right:
            # pylint is annoying here
            assert left

            left = left.next
            right = right.next

        # pylint is annoying here
        assert left
        assert left.next

        left.next = left.next.next
        return dummy.next

    def removeNthFromEndRecursive(
        self,
        head: Optional[ListNode],
        n: int,
    ) -> Optional[ListNode]:
        s = [0]
        return remove_impl(None, head, s, n)


def remove_impl(
    prev: Optional[ListNode],
    curr: Optional[ListNode],
    s: list[int],
    n: int,
) -> Optional[ListNode]:
    if not curr:
        return curr

    remove_impl(curr, curr.next, s, n)

    s[0] += 1

    if s[0] == n:
        if prev:
            prev.next = curr.next
            return prev

        return curr.next

    return curr


result = Solution().removeNthFromEnd(make_list([1, 2, 3, 4]), 2)
print(flatten_list(result))


result = Solution().removeNthFromEnd(make_list([5]), 1)
print(flatten_list(result))

result = Solution().removeNthFromEnd(make_list([1, 2]), 2)
print(flatten_list(result))
