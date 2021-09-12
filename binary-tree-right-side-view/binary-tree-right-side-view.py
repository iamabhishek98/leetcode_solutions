# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None: return []
        
        self.height = 0
        levels = [None]*101 # 101 because 100 is the max nodes in the tree
        
        def recurse(node = root, level = 0):
            if node is None: return
            self.height = max(self.height, level)
            
            if levels[level] is None: levels[level] = node.val
                
            recurse(node.right, level + 1)
            recurse(node.left, level + 1)
        
        recurse()
        return levels[:self.height + 1]
