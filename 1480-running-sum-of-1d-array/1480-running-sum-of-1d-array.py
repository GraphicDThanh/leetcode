class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        results = []
        for i, x in enumerate(nums):
            if i == 0:
                results.append(x)
            else:
                results.append(x + results[-1]) 
        
        return results