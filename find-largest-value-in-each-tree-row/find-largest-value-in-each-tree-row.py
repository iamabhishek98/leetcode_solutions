# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None: return []
        
        q = []
        q.append(root)
        q.append(None)
        ans = []
        m = -sys.maxint+1
        while q:
            curr = q.pop(0)
            if curr == None:
                ans.append(m)
                m = -sys.maxint+1
                q.append(None)
                if q[0] is None: break
            else:
                m = max(m,curr.val)
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
        
        return ans