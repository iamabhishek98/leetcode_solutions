# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        self.status = False
        
        def recurse(node, curr_sum = 0):
            if node:
                curr_sum += node.val
                
                if node.left is None and node.right is None and curr_sum == targetSum: 
                    self.status = True
                    return
                
                recurse(node.left, curr_sum)
                recurse(node.right, curr_sum)
                
        recurse(root)
        
        return self.status