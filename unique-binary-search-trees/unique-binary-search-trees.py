class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # https://leetcode.com/problems/unique-binary-search-trees/discuss/31666/DP-Solution-in-6-lines-with-explanation.-F(i-n)-G(i-1)-*-G(n-i)
        
        # top down dp approach
        # G(n): the number of unique BST for a sequence of length n.
        # F(i, n), 1 <= i <= n: the number of unique BST, where the number i is the root of BST
        # G(n) = F(1, n) + F(2, n) + ... + F(n, n). -> since there are n possible roots
        # F(i, n) = G(i-1) * G(n-i)	1 <= i <= n 
        # i-1 counts the no. of nodes on the left subtree (because all values have to be less than the parent)
        # n-i counts the no. of nodes on the right subtree (because all values have to be more than the parent)
        
        G = [0]*(n+1)
        # if there are 0 or 1 nodes, there can only be 1 possible unique BST
        G[0] = G[1] = 1
        
        for i in range(2,n+1):
            for j in range(1,i+1):
                G[i] += G[j-1]*G[i-j]
        
        return G[n]