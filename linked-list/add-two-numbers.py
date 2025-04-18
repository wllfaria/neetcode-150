from typing import Optional
from utils import ListNode, flatten_list, make_list


class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode],
    ) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sum = val1 + val2 + carry
            carry = sum // 10
            sum = sum % 10
            curr.next = ListNode(sum)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


result = Solution().addTwoNumbers(make_list([1, 2, 3]), make_list([4, 5, 6]))
print(flatten_list(result))

result = Solution().addTwoNumbers(make_list([9]), make_list([9]))
print(flatten_list(result))
