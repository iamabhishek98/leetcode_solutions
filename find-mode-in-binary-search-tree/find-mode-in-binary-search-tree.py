# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.m = {}
        self.max = -sys.maxint+1
        def recurse(node):
            if node is None: return
            if node.val not in self.m: self.m[node.val] = 1
            else: self.m[node.val]+=1
            if self.m[node.val] > self.max:
                self.max = self.m[node.val]
            recurse(node.left)
            recurse(node.right)

        recurse(root)
        ans = []
        for i in self.m:
            if self.m[i] == self.max:
                ans.append(i)
        return ans
        