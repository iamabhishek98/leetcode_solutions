from copy import copy

def binToDec(arr):
    ans = 0
    for i,x in enumerate(arr[::-1]):
        if x: ans += pow(2,i)
    return ans

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0
        self.ans = 0
        self.prev = []
        def recurse(node,path,s):
            if node is None:
                if path == self.prev and s is False: 
                    self.ans += binToDec(path)
                    self.prev = []
                else: self.prev = copy(path)
                return 
            path.append(node.val)
            recurse(node.left,path,True)
            recurse(node.right,path,False)
            path.pop()
        recurse(root,[],True)
        return self.ans