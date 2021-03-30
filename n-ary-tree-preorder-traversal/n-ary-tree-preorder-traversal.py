"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        self.arr = []
        def recurse(node):
            if node is None: return
            self.arr.append(node.val)
            for i in node.children:
                recurse(i)
        recurse(root)
        return self.arr
        