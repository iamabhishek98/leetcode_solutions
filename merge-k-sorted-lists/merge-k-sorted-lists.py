# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def merge2Lists(head1, head2):
            if not head1: return head2

            mergedList = ListNode()
            curr = mergedList
            
            while head1 or head2:
                if head1 and head2:
                    if head1.val <= head2.val:
                        curr.next = head1
                        head1 = head1.next
                    else: # head2.val < head1.val
                        curr.next = head2
                        head2 = head2.next
                    curr = curr.next
                    
                elif head2:
                    curr.next = head2
                    break
                else:
                    curr.next = head1
                    break
                    
            return mergedList.next
        
        interval = 1
        while interval < len(lists):
            for i in range(0, len(lists) - interval, interval*2):
                lists[i] = merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        
        return lists[0] if len(lists) else None
        