# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next: return True
        
        fast = head
        slow = head
        prev = None
        while fast and fast.next:
            # iterate twice as fast to reach end of the list
            fast = fast.next.next
            
            # reverse the first half of the linked list
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next
            
        # when fast is left at the last node of the list
        # this might happen when there are odd number of nodes in the list
        # we dont care about the middle node in palindromes so we skip it
        if fast:
            slow = slow.next
        
        while prev and prev.val == slow.val:
            slow = slow.next
            prev = prev.next
        
        # if it reached the end of the list, means all the comparisons were equal and so its a palindrome
        return not slow