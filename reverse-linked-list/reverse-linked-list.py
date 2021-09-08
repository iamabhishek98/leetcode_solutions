# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # recursion
        def recurse(head = head, prev = None):
            if head is None:
                return prev
            temp = head.next
            head.next = prev
            return recurse(temp, head)
        
        return recurse()
        
        # # iterative
        # prev = None
        # while head:
        #     temp = head.next
        #     head.next = prev
        #     prev = head
        #     head = temp
        # return prev
        