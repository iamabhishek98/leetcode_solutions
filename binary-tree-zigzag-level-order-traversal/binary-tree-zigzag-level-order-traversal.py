# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None: return []
        ans = []
        curr_i = -1
        queue = [(0,root)]
        ans.append([])
        while queue:
            curr = queue.pop(0)
            if curr_i != curr[0]:
                curr_i = curr[0]
                if curr_i == 0:
                    ans[-1] = ans[-1][::-1]
                else:
                    if curr_i%2==0: ans[-1] = ans[-1][::-1]
                    ans.append([])
            if curr[1]:
                ans[-1].append(curr[1].val)
                queue.append((curr_i+1,curr[1].left))
                queue.append((curr_i+1,curr[1].right))
        ans.pop()
        return ans