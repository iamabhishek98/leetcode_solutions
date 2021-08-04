# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        ans = []
        
        def recurse(node, arr = [], curr_sum = 0):
            # backtracking
            # append to add current element to array and pop to remove current element from array
            if node:
                arr.append(node.val)
                curr_sum += node.val
                
                if node.left is None and node.right is None:
                    if curr_sum == targetSum:
                        ans.append(arr[:])
                    arr.pop()
                    return
                
                recurse(node.left, arr, curr_sum)
                recurse(node.right, arr, curr_sum)
                
                curr_sum -= node.val
                arr.pop()
                
        recurse(root)
        
        return ans
        