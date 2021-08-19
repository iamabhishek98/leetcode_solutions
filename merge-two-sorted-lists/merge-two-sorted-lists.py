# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode()
        a = ans
        p1 = l1
        p2 = l2
        
        while p1 or p2:
            if p1 and p2:
                if p2.val < p1.val:
                    a.next = p2
                    p2 = p2.next
                else:
                    a.next = p1
                    p1 = p1.next
            elif p1:
                a.next = p1
                p1 = p1.next
            elif p2:
                a.next = p2
                p2 = p2.next
            a = a.next
        
        return ans.next

        