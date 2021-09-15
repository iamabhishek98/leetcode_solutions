# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/37154/8-lines-of-python-solution-(reverse-preorder-traversal)
        
        #         root
        #         / 
        #       1 
        #      / \ 
        #     3  4  
        #     Let's see what is happening with this code.

        #     Node(4).right = None
        #     Node(4).left = None
        #     prev = Node(4)
        #     Node(3).right = Node(4) (prev)
        #     Node(3).left = None
        #     prev = Node(3)->Node(4)
        #     Node(1).right = prev = Node(3) -> Node(4)
        #     Node(1).left = None
        #     prev = Node(1)->Node(3)->Node(4) (Which is the answer)
        
        # preorder: root -> left -> right
        # reverse preorder: right -> left -> root
        # postorder: left -> right -> root
        
        # therefore this is reverse preorder
        
        self.prev = None
        def recurse(root = root):
            if root is None: 
                return
            
            recurse(root.right)
            recurse(root.left)
            
            root.right = self.prev
            root.left = None
            # recursively building up the list on the right subtree through this assignment
            # references the right subtree first and then the left subtree references this right subtree...
            self.prev = root
            
        recurse()
