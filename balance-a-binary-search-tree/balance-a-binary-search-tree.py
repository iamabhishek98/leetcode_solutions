# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # first traverse the tree and store the elements in sorted manner (traverse inorder )
        # then to make Balance Binary search tree we need to make sure that
        # left child will be less than parent node
        # right child will be less than parent node

        # so take middle element of list make it Root and recursively assign its left side part
        # to root.left and its right part to root.right
        
        inorder_traversal = [] # inorder is sorted
        
        def inorder(node = root):
            if node is None: return
            
            inorder(node.left)
            inorder_traversal.append(node.val)
            inorder(node.right)
        
        inorder()
        
        def buildtree(start = 0, end = len(inorder_traversal)-1):
            if start > end: return
            mid = (start+end)/2
            parent = TreeNode(inorder_traversal[mid])
            parent.left = buildtree(start, mid-1)            
            parent.right = buildtree(mid+1, end)
            
            return parent
        
        return buildtree()