# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p1 = head
        for i in range(n-1):
            p1 = p1.next
        
        if p1 == head and p1.next is None: return
        
        p2 = None
        prev = p2
        while p1.next is not None:
            if p2 is None: p2 = head
            prev = p2
            p1 = p1.next
            p2 = p2.next
        
        if p2 is None: return head.next
        prev.next = p2.next
        return head
            
            