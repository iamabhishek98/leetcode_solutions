class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # build circular linked list
        head = ListNode()
        itr = head
        for i in range(1,n+1):
            itr.next = ListNode(i)
            itr = itr.next
        itr.next = head.next
        
        itr = head.next
        count = 0
        while count < n-1:
            # traverse to the node to be remove
            for i in range((k-1)%n):
                itr = itr.next
            
            # delete current node
            itr.val = itr.next.val
            itr.next = itr.next.next
            
            # move on to next iteration of game
            count += 1    
        
        return itr.val
        
        