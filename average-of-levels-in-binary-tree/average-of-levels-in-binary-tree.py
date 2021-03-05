
    
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        self.ans = []
        self.arr = []
        
        def getSum(arr):
            s = 0
            for i in arr:
                s += i.val
            return s
        
        def compute(root):
            if root is None: return
            queue = []
            queueChild = []
            
            queue.append(root)
            self.ans.append(root.val)
            count = 0
            curr_index = 0
            while queue or queueChild:
                if not queue: 
                    queue = queueChild
                    self.ans.append(getSum(queueChild)/float(len(queueChild)))
                    queueChild = []
                node = queue.pop(0)
                
                if node.left is not None:
                    queueChild.append(node.left)
                if node.right is not None:
                    queueChild.append(node.right)
        compute(root)
            
        return self.ans
        