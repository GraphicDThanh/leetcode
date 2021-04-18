[46. Permutations](https://leetcode.com/problems/permutations/)

**Solution:**

Explanation:
- With n is length of the list, will have n! permutation
  n! = n * (n-1) * (n-2) * ... * 1
By example: [1, 2, 3]

We want permutation with length is length of the list, is 3, then we have 3 positions to put value on: _  _  _

- At position 1, permutation = _ _ _ ; choices = [1, 2, 3]
  - If select 1, -> permutation = 1 _ _ ; choices = [2, 3]
    - If select 2 -> permutation = 1 2 _ ; choices = [3]
        - If select 3 -> permutation = 1 2 3 ; choices = [] -> no more choice
            > append permutation [1, 2, 3] to result
    - If select 3 -> permutation = 1 3 _ ; choices = [2]
        - If select 2 -> permutation = 1 3 2 ; choices = [] -> no more choice
            > append permutation [1, 3, 2] to result
  - If select 2, the choices will reduce to [1, 3]
    - If select 1 -> permutation = 2 1 _ ; choices = [3]
        - If select 3 -> permutation = 2 1 3 ; choices = [] -> no more choice
            > append permutation [2, 1, 3] to result
    - If select 3 -> permutation = 2 3 _ ; choices = [1]
        - If select 1 -> permutation = 2 3 1 ; choices = [] -> no more choice
            > append permutation [2, 3, 1] to result
  - If select 3, the choices will reduce to [1, 2]
    - If select 1 -> permutation = 3 1 _ ; choices = [2]
        - If select 2 -> permutation = 3 1 2 ; choices = [] -> no more choice
            > append permutation [3, 1, 2] to result
    - If select 2 -> permutation = 3 2 _ ; choices = [1]
        - If select 1 -> permutation = 3 2 1 ; choices = [] -> no more choice
            > append permutation [3, 2, 1] to result


> If still have choice, get next value and put to permutation, then pop them out of the choices
>
> If no more choice, append permutation to results.


Analysis:
- Time complexity: O(n!)
- Space complexity: O(n!) permutations and O(n!) for choices -> O(n!) * O(n!) (?)

Submission Detail
```
Status: Accepted
25 / 25 test cases passed.
Runtime: 24 ms
Memory Usage: 13.4 MB
```

```python
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
            else:****
                self.find_permutation(permutation_copy, choices_copy, results)
```