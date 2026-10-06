class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = []
    
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                profits.append(profit)
    
    # If no profits were added (empty list), return 0
    # Otherwise return the maximum profit, but at least 0
        return max(max(profits), 0) if profits else 0