# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return TreeNode(val)
        self.status = False
        ans = root
        def insert(node,val):
            if self.status: return
            if val > node.val:
                if node.right: insert(node.right,val)
                else:
                    node.right = TreeNode(val)
                    self.status = True
                    return
            elif val < node.val:
                if node.left: insert(node.left,val)
                else:
                    node.left = TreeNode(val)
                    self.status = True
                    return
        insert(root,val)
        return ans
                
        