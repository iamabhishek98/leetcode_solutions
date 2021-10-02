class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # Method 1: Tabulation (Top down DP approach)
        dp = [[0 for _ in range(n+1)] for __ in range(m+1)]
        dp[1][1] = 1
        
        for i in range(m+1):
            for j in range(n+1):
                # add to bottom cell
                if i+1 <= m: dp[i+1][j] += dp[i][j]
                # add to right cell
                if j+1 <= n: dp[i][j+1] += dp[i][j]
        
        return dp[m][n]
        
#         # Method 2: Memoization (Bottom up DP approach)
#         memo = {}
        
#         def recurse(m = m, n = n):
#             # base case: reached finish cell
#             if m == 1 and n == 1: return 1
#             # base case: not possible
#             if m == 0 or n == 0: return 0
            
#             key = str(m)+":"+str(n)
#             if key in memo: return memo[key]
            
#             # travel down or to the right
#             memo[key] = recurse(m-1,n) + recurse(m,n-1) 
#             return memo[key]
        
#         return recurse()