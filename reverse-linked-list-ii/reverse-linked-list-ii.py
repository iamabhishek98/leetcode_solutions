# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head: return
        if m == n: return head
        
        curr = head
        prev = None
        
        for _ in range(m-1):
            prev = curr
            curr = curr.next
            n -= 1
        
        tail = curr
        conn = prev
        
        for _ in range(n):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        if conn:
            conn.next = prev
        else:
            head = prev
        
        tail.next = curr
        
        return head
        