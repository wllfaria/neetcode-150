class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            value = numbers[left] + numbers[right]

            if value == target:
                return [left + 1, right + 1]

            if value > target:
                right -= 1

            if value < target:
                left += 1

        return []
