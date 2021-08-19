# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxProduct(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # https://www.youtube.com/watch?v=8WL9lUp8EvE&ab_channel=LeadCodingbyFRAZ
        
        def getSum(node = root):
            if not node: return 0
            return node.val + getSum(node.left) + getSum(node.right)
    
        total = getSum()
        
        self.max_product = 0
        
        def recurse(node = root):
            if not node: return 0
            
            left = recurse(node.left)
            right = recurse(node.right)
            
            # the entire subtree above the current node
            up = total - (node.val + left + right)
            
            # remove top edge
            op1 = up * (node.val + left + right)
            
            # remove left edge
            op2 = left * (node.val + up + right)
            
            # remove right edge
            op3 = right * (node.val + up + left)
            
            self.max_product = max(self.max_product, op1, op2 , op3)
            
            # returns the sum of the current subtree
            return node.val + left + right
        
        recurse()
        
        return self.max_product % (pow(10,9)+7)