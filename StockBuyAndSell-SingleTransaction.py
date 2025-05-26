class Solution:
    def maximumProfit(self, prices):
        # code here
        min_price=9999
        max_prof=0
        for i in prices:
            if i<min_price:
                min_price=i
            else:
                profit=i-min_price
                max_prof=max(max_prof,profit)
        return max_prof