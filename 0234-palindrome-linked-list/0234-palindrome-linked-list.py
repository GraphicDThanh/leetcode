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