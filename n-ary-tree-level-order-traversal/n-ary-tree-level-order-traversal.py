"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root is None: return []
        ans = []
        curr_i = -1
        queue = [(0,root)]
        while queue:
            curr = queue.pop(0)
            if curr_i != curr[0]: 
                curr_i = curr[0]
                ans.append([])
            if curr[1]:
                ans[-1].append(curr[1].val)
                for c in curr[1].children:
                    queue.append((curr_i+1,c))
        return ans
