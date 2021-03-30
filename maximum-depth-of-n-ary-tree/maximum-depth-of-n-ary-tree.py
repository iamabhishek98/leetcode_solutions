"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None: return 0
        def recurse(node,lvl):
            if node is None: return 0
            m = 0
            for i in node.children:
                h = recurse(i,lvl+1)+1
                m = max(m,h)
            return m
        return recurse(root,0)+1
        