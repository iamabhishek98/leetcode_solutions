"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None: return root
        
        q = []
        q.append(root)
        count = 0
        start = 1
        right = []
        while q:
            curr = q.pop(0)
            count += 1
            if count == pow(2,start):
                right.append(None)
                start+=1
            right.append(curr)
            if curr.left: q.append(curr.left)
            if curr.right: q.append(curr.right)
        right.append(None)
        
        p = 0
        count = 0
        start = 1
        q.append(root)
        while q:
            curr = q.pop(0)
            count += 1
            p+=1
            if count == pow(2,start):
                right.append(None)
                start+=1
                p+=1
            curr.next = right[p]
            if curr.left: q.append(curr.left)
            if curr.right: q.append(curr.right)
        
        return root
            
        