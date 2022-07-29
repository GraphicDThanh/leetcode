class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # O(n) solution
#         for i, n in enumerate(nums):
#             if n == target:
#                 return i
            
        # O(logn) solution
        # base on ascending order:
        # if the middle of the list smaller then target 
        # > move start to mid + 1
        # if the middle of the list larger then target 
        # > move end to mid - 1
        
        start, end = 0, len(nums) - 1

        while start <= end:
            middle = int((start + end) / 2)

            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                start = middle + 1
            else:
                end = middle - 1
        
        return -1