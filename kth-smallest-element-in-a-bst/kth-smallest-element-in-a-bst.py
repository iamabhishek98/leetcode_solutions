# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        ori = root
        x = root.val
        while (k):
            root = ori
            if (root.left is None):
                x = root.val
                ori = root.right
            elif (root.left is None and root.right is None):
                x = root.val
                break
            else:
                while(root):
                    if (root.left.left is None and root.left.right is None):
                        x = root.left.val
                        root.left = None
                        break
                    elif (root.left.left is None):
                        x = root.left.val
                        root.left = root.left.right
                        break
                    else: root = root.left
            k-=1
        return x
        