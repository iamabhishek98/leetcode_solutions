# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        self.x = TreeNode()
        ans = self.x
        
        def recurse(root):
            if root:
                recurse(root.left)
                self.x.right = TreeNode(root.val)
                self.x = self.x.right 
                recurse(root.right)
        
        recurse(root)
        
        return ans.right
        