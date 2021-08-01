# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        seq1 = []
        self.seq2_count = 0
        
        self.status = True
        def recurse(id, node):
            if node is not None:
                if not node.left and not node.right:
                    if id == 1: seq1.append(node.val)
                    else: self.seq2_count += 1
                        
                    if self.seq2_count > len(seq1) or (node.val != seq1[self.seq2_count-1]): self.status = False
                    return
                
                recurse(id, node.left) 
                recurse(id, node.right)
        
        recurse(1,root1)
        recurse(2,root2)
        
        if len(seq1) != self.seq2_count: return False
        return self.status