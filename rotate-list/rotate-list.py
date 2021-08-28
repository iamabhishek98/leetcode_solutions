# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        temp_head = head
        self.n = 0
        
        # 501 because 500 is the maximum number of nodes in a list
        def reverse(end = 501):
            prev = None
            curr = self.reverse_head
            while curr and end:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                self.n += 1
                end -= 1
            self.reverse_head = prev
            return curr
        
        # reverse entire list
        self.reverse_head = head
        reverse()
        
        if not self.n: return
        
        k %= self.n
        # reverse first k elements and return head of second half
        second_half = reverse(k)
        
        # reverse second half
        temp_head = self.reverse_head
        self.reverse_head = second_half
        reverse()
        
        # iterate through first half and attach second half to next of last element of first half
        ans = temp_head
        if temp_head:
            while temp_head:
                if temp_head.next is None: 
                    temp_head.next = self.reverse_head
                    break
                else: temp_head = temp_head.next
        else:
            ans = self.reverse_head
            
        return ans