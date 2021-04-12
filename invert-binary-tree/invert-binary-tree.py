def invert(root):
    if (root is None): return None
    right = invert(root.right)
    left = invert(root.left)
    root.right = left
    root.left = right
    return root

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return invert(root)