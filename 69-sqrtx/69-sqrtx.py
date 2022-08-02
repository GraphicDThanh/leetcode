class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # sqrt(x) = k means k*k = x
        # use binary search from 0 to x, if k * k = x then return k
        if x == 0:
            return 0
        if x == 1:
            return 1
        
        left, right = 0, x
        
        while left < right:
            mid = left + (right - left) // 2
            
            if round(mid * mid, 2) <= x:
                left = mid + 1
            else:
                right = mid
        
        return left - 1
        
        