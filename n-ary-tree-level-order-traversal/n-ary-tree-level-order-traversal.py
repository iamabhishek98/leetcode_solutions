"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root: return []
        
        levels = {}
        
        q = deque()
        
        q.append([0,root])
        
        currLvl = []
        
        # bfs to iterate lvl by lvl
        while q:
            curr = q.popleft()    
            lvl = curr[0]
            val = curr[1].val
            
            if lvl in levels: levels[lvl].append(val)
            else: levels[lvl] = [val]
            
            for child in curr[1].children:
                q.append([lvl+1,child])
        
        return levels.values()