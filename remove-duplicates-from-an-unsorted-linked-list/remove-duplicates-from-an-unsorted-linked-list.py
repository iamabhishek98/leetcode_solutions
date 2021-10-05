# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicatesUnsorted(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        freq = {}
        head1 = head
        while head1:
            freq[head1.val] = freq.get(head1.val,0) + 1
            head1 = head1.next

        while head and freq[head.val] > 1:
            head = head.next
            
        head2 = head
        while head2 and head2.next:
            while head2 and head2.next and freq[head2.next.val] > 1:
                if head2.next.next:
                    nxt = head2.next.next
                    head2.next = nxt
                else:
                    head2.next = None
            
            if head2:    
                head2 = head2.next            
        
        return head