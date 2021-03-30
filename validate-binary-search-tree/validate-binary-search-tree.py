# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.status = True
        def check(node,parentRight, parentLeft):
            if node is None: return
            for i in parentRight:
                if node.val <= i:
                    self.status = False
                    return
            for i in parentLeft:
                if node.val >= i:
                    self.status = False
                    return
            check(node.left,parentRight,parentLeft+[node.val])
            check(node.right,parentRight+[node.val],parentLeft)
            
        check(root,[],[])
        return self.status    