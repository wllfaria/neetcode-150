from typing import Optional
from utils import ListNode, flatten_list, make_list


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        node = ListNode()
        dummy = node

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next

            node = node.next

        node.next = list1 or list2

        return dummy.next


result = Solution().mergeTwoLists(make_list([1, 2, 3]), make_list([1, 2, 3]))
assert flatten_list(result) == [1, 1, 2, 2, 3, 3]

result = Solution().mergeTwoLists(make_list([]), make_list([1, 2, 3]))
assert flatten_list(result) == [1, 2, 3]

result = Solution().mergeTwoLists(make_list([]), make_list([]))
assert flatten_list(result) == []
