def getHeight(node):
    if node is None: return 0
    return max(getHeight(node.right),getHeight(node.left))+1

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sum = 0
        self.height = getHeight(root)
        self.node = TreeNode()
        def recurse(node,h):
            if node is None: return
            if node.left is None and node.right is None and h == self.height:
                self.node = node
                return True
            a = recurse(node.left,h+1)
            b = recurse(node.right,h+1)
            if a and b: self.node = node
            if a or b: return True
        
        recurse(root,1)
        return self.node