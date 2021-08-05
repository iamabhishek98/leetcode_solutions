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
        # idea: two pointers p1 and p2 which are spaced n distance apart
        
        p1 = head
        # loops only until n-1 because when p1 is at nth position, we want p2 to start at beginning of list (at head)
        # we only want to do this in the 2nd while loop
        for i in range(n-1):
            p1 = p1.next
        
        # return nothing because this implies length of linked list is only 1 and we need to remove the one and only node
        if p1 == head and p1.next is None: return
        
        p2 = None
        prev = p2
        while p1.next is not None:
            if p2 is None: p2 = head
            prev = p2
            p1 = p1.next
            p2 = p2.next
        
        # if p2 is None that means the nth node is actually head
        if p2 is None: return head.next
        
        # if not skip p2 (because p2 is the nth node)
        prev.next = p2.next
        return head
            
            