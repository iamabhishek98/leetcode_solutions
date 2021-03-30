"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        self.arr = []
        def recurse(node):
            if node is None: return
            for i in node.children:
                recurse(i)
            self.arr.append(node.val)
        recurse(root)
        return self.arr
        