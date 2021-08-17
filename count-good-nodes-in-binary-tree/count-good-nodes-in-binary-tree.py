# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0
        
        def recurse(node = root, curr_max = root.val):
            if node is None:
                return
            
            if node.val >= curr_max:
                self.count += 1
                curr_max = max(node.val, curr_max)
            
            recurse(node.left, curr_max)            
            recurse(node.right, curr_max)
        
        recurse()
        return self.count