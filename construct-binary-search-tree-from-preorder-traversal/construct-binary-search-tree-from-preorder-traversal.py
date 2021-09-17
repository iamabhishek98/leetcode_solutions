# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        self.i = 0
        
        def construct(upper_bound = sys.maxint):
            # if the current value is more than the upper bound, then we skip it
            if self.i >= len(preorder) or preorder[self.i] >= upper_bound: return None

            # preorder always starts with the root: root -> left -> right
            root = TreeNode(preorder[self.i])
            
            # to traverse the preorder array
            # when we are done traversing the left subtree, the index will be at the correct position for right subtree
            self.i += 1
            
            # left subtree's upper bound is the parent value
            root.left = construct(root.val)
            # there is no upper bound in the right subtree which is why we use the max int val
            root.right = construct(upper_bound)

            # after building the tree recursively, we return the root
            return root
        
        return construct()
                
            