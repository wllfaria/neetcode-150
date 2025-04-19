class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            # cycle detected
            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

    def findDuplicateHashSet(self, nums: list[int]) -> int:
        seen: set[int] = set()

        for n in nums:
            if n in seen:
                return n

            seen.add(n)

        return -1


print(Solution().findDuplicate([1, 2, 3, 2, 2]))
print(Solution().findDuplicate([1, 2, 3, 4, 4]))
