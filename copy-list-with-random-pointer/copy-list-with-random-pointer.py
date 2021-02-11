"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if (head is None): return None
        elif head.next is None: 
            ans = Node(head.val,None,None)
            if (head.random is None): return ans
            ans.random = ans
            return ans
        copy = Node(head.val)
        ans = copy
        start = head
        start = start.next
        while (start):
            new = Node(start.val)
            copy.next = new
            copy = copy.next
            start = start.next
        
        start = head
        copy = ans
        i = 0
        while(start):
            temp = start.next
            start.next = copy
            copy.random = start
            start = temp
            copy = copy.next
            i+=1
            
        copy = ans
        while (copy):
            copy.random = copy.random.random.next if copy.random.random is not None else None
            copy = copy.next
        
        return ans