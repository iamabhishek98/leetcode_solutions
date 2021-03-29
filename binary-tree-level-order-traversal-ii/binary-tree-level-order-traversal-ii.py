# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None: return []
        ans = []
        curr_i = -1
        queue = [(0,root)]
        while queue:
            curr = queue.pop(0)
            if curr_i != curr[0]: 
                curr_i = curr[0]
                ans.append([])
            if curr[1]:
                ans[-1].append(curr[1].val)
                queue.append((curr_i+1,curr[1].left))
                queue.append((curr_i+1,curr[1].right))
        ans.pop()
        return ans[::-1]
        