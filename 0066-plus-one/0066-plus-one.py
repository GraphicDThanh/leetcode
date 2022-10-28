class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = [str(i) for i in digits]
        digits = str(int(''.join(digits)) + 1)
        return [int(i) for i in digits]