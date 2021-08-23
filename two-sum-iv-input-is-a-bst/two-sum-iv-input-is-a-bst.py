# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        # approach 1: use a set which has all the stored values as you iterate through the tree and look for k - curr.val 
        # approach 2: use binary search (implemented method)
        
        if not root.left and not root.right: return False
        
        def dfs(node = root, value = k):
            if node is None: return False
            return binarySearch(root, node, k - node.val) or dfs(node.left) or dfs(node.right)
        
        def binarySearch(node, curr, value):
            if node is None: return False
            if node != curr:
                return node.val == value or binarySearch(node.left, curr, value) or binarySearch(node.right, curr, value) 
            return False
        
        return dfs()