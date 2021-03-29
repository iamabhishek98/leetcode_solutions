# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.arr = []
        def recurse(node):
            if node is None: return
            recurse(node.left)
            recurse(node.right)
            self.arr.append(node.val)
        recurse(root)
        return self.arr
        