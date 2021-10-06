class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # top down memoization approach
        memo = {}
        def recurse(i = n):
            if i == 1: return k
            if i == 2: return k**2
            
            if i in memo: return memo[i]
            
            memo[i] = (k-1)*(recurse(i-1)+recurse(i-2))
            return memo[i]
        
        return recurse()
            
            
            