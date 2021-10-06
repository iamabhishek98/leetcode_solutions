# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # there are 2^k-1 nodes for a complete binary tree of depth k
        
        # since it is a complete tree, the max level is the leftmost path
        def compute_depth(node = root, left_extreme=True):
            if node is None: return 0
            if left_extreme:
                return 1+compute_depth(node.left,left_extreme)
            return 1+compute_depth(node.right,left_extreme)
        
        def recurse(node = root):
            if node is None: return 0
            
            left_extreme_depth = compute_depth(node)
            right_extreme_depth = compute_depth(node,False)
            
            # then we know subtree is complete so the total number of nodes is 2^k-1
            if left_extreme_depth == right_extreme_depth:
                return pow(2,left_extreme_depth)-1
            
            # if leftmost and rightmost paths are not equal we know the subtree is not complete 
            # so we recurse to the children of the current node to get the next complete subtree
            # we add 1 here to include the current node along with the ans from its children
            return 1+recurse(node.left)+recurse(node.right)
        
        return recurse()