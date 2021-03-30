from copy import deepcopy

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.arr = []
        self.curr = -1
        self.recurse(root)
    
    def recurse(self,node):
        if node is None: return
        self.recurse(node.left)
        self.arr.append(node.val)
        self.recurse(node.right)
        
    def next(self):
        """
        :rtype: int
        """
        self.curr+=1
        return self.arr[self.curr]
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return (self.curr+1)!=len(self.arr)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()