# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        # https://leetcode.com/problems/unique-binary-search-trees-ii/discuss/31495/Should-be-6-Liner
        
        dp = {}
        
        def generate(start = 1, end = n):
            key = (start,end) # tuple
            if key in dp: return dp[key]

            # need to return None because start cannot be more than the end (because its a BST)
            if start > end: 
                return [None]
            
            trees = []
            # uses all values from 1 to n as root
            for root in range(start, end+1):
                # generates and loops through all left subtrees (values lesser than the parent)
                for left in generate(start, root - 1):
                    # generates and loops through all right subtrees (values greater than the parent)
                    for right in generate(root + 1, end):
                        node = TreeNode(root, left, right)
                        trees.append(node)
                        
            dp[key] = trees
            return trees
        
        return generate()
        