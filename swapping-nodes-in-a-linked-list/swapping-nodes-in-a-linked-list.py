# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        ans = head
        count = 0
        first_val = 0
        while head:
            if count == k-1:
                first_val = head.val
            count += 1
            head = head.next
        head = ans
        pos = count - k
        count = 0
        second_val = 0
        while head:
            if count == pos:
                second_val = head.val
                head.val = first_val
            count += 1
            head = head.next
        head = ans
        count = 0
        while head:
            if count == k-1:
                head.val = second_val
            count += 1
            head = head.next
        return ans