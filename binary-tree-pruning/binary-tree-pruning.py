# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """        
        ans = root
        def recurse(node):
            left = False
            if node.left:
                left = recurse(node.left)
                if not left:
                    node.left = None
            
            right = False
            if node.right:
                right = recurse(node.right) 
                if not right:
                    node.right = None
                    
            if node.val or left or right: return True
            node = None
            return False
        
        recurse(root)
        if not ans.val and not ans.left and not ans.right: return None
        return ans
        