# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.l = TreeNode(0)
        self.arr = []
        def dfs(node):
            if node is None:
                return
            self.arr.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        ans = root
        for i,x in enumerate(self.arr):
            root.val = x
            root.left = None
            root.right = None
            if i < len(self.arr)-1:
                root.right = TreeNode()
                root = root.right