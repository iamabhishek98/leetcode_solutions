# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ans = []
        
        if (root is None): return ans
        if (root.right is None and root.left is None): return [root.val]
        
        queue = []
        queue.append(root)
        
        while queue:
            s = len(queue)
            for i in range(s):
                curr = queue[0]
                queue.pop(0)
                if (i == s-1):
                    ans.append(curr.val)
                if (curr.left):
                    queue.append(curr.left)
                if (curr.right):
                    queue.append(curr.right)
        return ans
            