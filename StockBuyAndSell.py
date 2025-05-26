from typing import List


class Solution:
    def maximumProfit(self, prices) -> int:
        # code here
        profits=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                profits+=prices[i]-prices[i-1]
        return profits
