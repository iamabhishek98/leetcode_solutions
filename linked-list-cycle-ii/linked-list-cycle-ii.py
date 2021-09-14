# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return
        
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
            if fast: fast = fast.next
            if fast == slow:
                while slow != head:
                    slow = slow.next
                    head = head.next
                return head
        
        return
        