# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # storing the preorder traversal in a string
        s = []
        def dfs(node = root):
            if node is None:
                s.append("#")
                return
            s.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs()
        return ",".join(s)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return
        queue = deque(data.split(","))
        
        # reconstructing bst by traversing the nodes in the preorder traversal and assigning values
        def construct():
            if queue:
                curr = queue.popleft()
                if curr == "#": return
                root = TreeNode(int(curr))
                root.left = construct()                
                root.right = construct()
                return root
        
        return construct()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))