from collections import deque

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        q = deque()
        
        while head:
            q.append(head.val)
            head = head.next
            
        ans = 0
        while q:
            i = q.popleft()
            if i: ans += pow(2,len(q))
        
        return ans