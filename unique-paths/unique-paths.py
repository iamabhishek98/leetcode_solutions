class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        memo = {}
        
        def recurse(m = m, n = n):
            # base case: reached finish cell
            if m == 1 and n == 1: return 1
            # base case: not possible
            if m == 0 or n == 0: return 0
            
            key = str(m)+":"+str(n)
            if key in memo: return memo[key]
            
            # travel down or to the right
            memo[key] = recurse(m-1,n) + recurse(m,n-1) 
            return memo[key]
        
        return recurse()