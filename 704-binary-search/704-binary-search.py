class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """   
        # O(logn) solution
        # base on ascending order:
        # if the middle of the list smaller then target 
        # > move start to mid + 1
        # if the middle of the list larger then target 
        # > move end to mid - 1
        length_nums = len(nums)
        
        if length_nums == 0:
            return -1
        
        if length_nums == 1:
            if nums[0] == target:
                return 0
            return -1
        
        start, end = 0, len(nums) - 1

        while start <= end:
            middle = int((start + end) / 2)
            num_middle = nums[middle]
            if num_middle == target:
                return middle
            elif num_middle < target:
                start = middle + 1
            else:
                end = middle - 1
        
        # not found
        return -1