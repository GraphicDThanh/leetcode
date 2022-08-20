class Solution:
    def arrangeCoins(self, n: int) -> int:
        rows = 1
        while n > 0:
            rows = rows + 1
            n = n - rows
        
        return rows - 1
    