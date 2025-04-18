class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) == 1:
            return 0

        left = 0
        right = 1

        max_profit = 0

        while right < len(prices):
            val = prices[left]

            if prices[right] > val:
                max_profit = max(max_profit, prices[right] - val)
            else:
                left = right

            right += 1

        return max_profit
