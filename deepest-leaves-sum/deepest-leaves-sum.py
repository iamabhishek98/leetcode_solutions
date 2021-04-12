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
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = 0
        self.height = getHeight(root)
        
        def recurse(node,h):
            if node is None: return
            if node.left is None and node.right is None and h == self.height:
                self.sum += node.val
                return
            recurse(node.left,h+1)
            recurse(node.right,h+1)
        
        recurse(root,1)
        return self.sum
                