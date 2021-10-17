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
        :rtype: int
        """
        curr_path_sum_map = defaultdict(int)
        self.count = 0
        
        def preorder(node = root, curr_sum = 0):
            if not node: return
            
            curr_sum += node.val
            
            # check the sum at every stage
            if curr_sum == targetSum: self.count += 1
            
            # check if the difference exists in the previous parts of the path
            self.count += curr_path_sum_map[curr_sum - targetSum]
            
            # include the current sum in the current subtree before traversing to the child
            curr_path_sum_map[curr_sum] += 1
            
            preorder(node.left, curr_sum)
            preorder(node.right, curr_sum)

            # remove the current sum before traversing back to the parent
            curr_path_sum_map[curr_sum] -= 1  
        
        preorder()
        return self.count