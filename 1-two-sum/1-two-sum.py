class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        visited = {}
        for i, n in enumerate(nums):
            if target - n in visited.keys() and i > 0:
                return i, visited[target - n]
            
            visited[n] = i
        
        