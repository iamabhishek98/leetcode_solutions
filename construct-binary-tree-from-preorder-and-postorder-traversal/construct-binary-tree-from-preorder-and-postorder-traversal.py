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
        self.preIndex = 0
        def recurse(startPostOrder = 0, endPostOrder = len(postorder)):
            if self.preIndex >= len(preorder) or startPostOrder > endPostOrder: return
            
            root = TreeNode(preorder[self.preIndex])
            self.preIndex += 1
            
            if startPostOrder == endPostOrder or self.preIndex >= len(preorder): return root
            
            found = False
            for i in range(startPostOrder, endPostOrder):
                if postorder[i] == preorder[self.preIndex]:
                    found = i
                    break
                    
            if found <= endPostOrder:
                root.left = recurse(startPostOrder, found)
                root.right = recurse(found + 1, endPostOrder - 1)
            
            return root
            
        return recurse()