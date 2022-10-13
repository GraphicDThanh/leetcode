class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []

        self.find_permutation([], nums, results)

        return results

    def find_permutation(self, permutation, choices, results):
        for j, m in enumerate(choices):
            choices_copy = choices[::]
            permutation_copy = permutation[::]
            choices_copy.pop(j)
            permutation_copy.append(m)

            if len(choices_copy) == 0:
                results = results.append(permutation_copy)
                return results
            else:
                self.find_permutation(permutation_copy, choices_copy, results)