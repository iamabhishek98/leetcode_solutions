# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # https://www.youtube.com/watch?v=GeltTz3Z1rw
        
        def recurse(preStart, inStart, inEnd):
            if preStart >= len(preorder) or inStart > inEnd: return
            
            root = TreeNode(preorder[preStart])
            
            # find index of the preorder root in the inorder array
            inIndex = 0
            for i in range(inStart,inEnd+1):
                if inorder[i] == root.val:
                    inIndex = i
                    break
            
            # to skip the current root and go to the root of the left subtree
            # boundary updated to from inorder start to just before index of preorder root
            root.left = recurse(preStart + 1, inStart, inIndex-1)
            
            # to skip the current root and the left subtree and go the root of the right subtree
            # boundary updated to from just after inorder start to inorder end
            root.right = recurse(preStart + (inIndex - inStart) + 1, inIndex + 1, inEnd)
            
            return root
        
        return recurse(0,0,len(inorder)-1)