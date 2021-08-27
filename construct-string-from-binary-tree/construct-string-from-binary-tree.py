# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node = root):
            if node is None: 
                return ""
            
            # no need for parenthesis in this case
            if not node.left and not node.right:
                return str(node.val)
            
            # can ignore node.right
            if not node.right:
                return str(node.val)+"("+dfs(node.left)+")"
            
            # need to consider all children
            return str(node.val)+"("+dfs(node.left)+")"+"("+dfs(node.right)+")"
        
        return dfs()