# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        self.curr_min = sys.maxint
        self.closest = root.val
        
        def recurse(node = root):
            if node is None: return
            
            curr_dist = abs(node.val-target)
            
            if curr_dist < self.curr_min:
                self.curr_min = curr_dist
                self.closest = node.val
                
            if target < node.val:
                recurse(node.left)
            else:
                recurse(node.right)            
        
        recurse()
        return self.closest