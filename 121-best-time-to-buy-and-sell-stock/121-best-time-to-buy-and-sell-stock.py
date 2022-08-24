# **Solution 2: 2 pointer**
# - Use 2 pointers: left, right. maxProfile start with 0
# - Start with left is the first day, right is the second day
# - If profit > maxProfile then:
#   - set new maxProfit
#   - keep the left and move the right pointer to the next day of the right to check with maxProfit
#   - if profit < maxProfit:
#     -  keep the left and move the right pointer to the next day of the right
#  - else:
#    - set maxProfit
#    - keep the left and move the right pointer to the next day of the right to check with maxProfit
# - If profit < maxProfit then:
#   - move the left to the next day of the left
#   - move the right to the next day of the right
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_profit = 0
        
        while r < len(prices):
            # only check if left price small than right price to set max profile
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                if profit > max_profit:
                    max_profit = profit
            else:
                # if left price bigger then right price then move left to smaller price
                l = r
            
            # always move right to the next price of right
            r += 1
        return max_profit