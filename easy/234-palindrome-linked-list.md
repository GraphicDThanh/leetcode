[234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

**Solution 1:**

Explanation:
- Save all value of linked list to an array
- Reverse array and compare with the original
- If true, it is a palindrome

Analysis:
- Time complexity: O(n)
- Space complexity: O(n)

Submission Detail
```
Status: Accepted
85 / 85 test cases passed.
Runtime: 1152 ms
Memory Usage: 85.2 MB
```

```python
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        node = head
        stack = [head.val]

        while node.next:
            stack.append(node.next.val)
            node = node.next

        stack_reversed = stack[::-1]

        if stack_reversed == stack:
            return True

        return False
```

**Solution 2:**

Explanation:
- Use fast(2 steps) and slow(1 step) pointers to find the middle of the linked list
  - The idea is when fast pointer will get to the end of linked list is the time slow pointer in the middle of the list
- After defining the middle one, we go and reverse the a half of the linked list
- After reverse, if the reversed match other then it is a palindrome linked list

Analysis:
- Time complexity: O(n)
- Space complexity: O(2)

Submission Detail
```
```

```python
```