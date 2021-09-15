# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        indexes = {}
        for i,x in enumerate(postorder):
            indexes[x] = i
        
        self.preIndex = 0

        def recurse(startPostOrder = 0, endPostOrder = len(postorder)):
            if self.preIndex >= len(preorder) or startPostOrder > endPostOrder: return
            
            root = TreeNode(preorder[self.preIndex])
            self.preIndex += 1
            
            if self.preIndex >= len(preorder) or startPostOrder == endPostOrder: return root
            
            # search for the index of the root of the left subtree in the postorder traversal
            search = indexes[preorder[self.preIndex]]
            leftIndex = search if startPostOrder <= search < endPostOrder else startPostOrder 
            
            root.left = recurse(startPostOrder, leftIndex)
            root.right = recurse(leftIndex + 1, endPostOrder - 1)
            
            return root
            
        return recurse()