# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        def dfs(self,target, original_node,cloned_node):
            if (original_node is None): return
            if (original_node is target):
                return cloned_node
            return dfs(self,target,original_node.left,cloned_node.left) or dfs(self,target,original_node.right,cloned_node.right)

        return dfs(self,target,original,cloned)
        