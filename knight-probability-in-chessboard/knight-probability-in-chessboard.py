class Solution(object):
    def knightProbability(self, n, k, row, column):
        """
        :type n: int
        :type k: int
        :type row: int
        :type column: int
        :rtype: float
        """
        # Method: Bottom up memoization approach
        possible_moves = [[2,1],[2,-1],[1,2],[1,-2],[-2,1],[-2,-1],[-1,2],[-1,-2]]
        
        dp = {}
        
        def recurse(i=row, j=column, count=0):
            if i < 0 or i >= n or j < 0 or j >= n:
                return 0.0
            
            if count == k:
                return 1.0
            
            key = str(i)+":"+str(j)+":"+str(count)
            if key in dp: return dp[key]
            
            ans = 0.0
            for move in possible_moves:
                ans += recurse(i+move[0],j+move[1],count+1)
            
            dp[key] = ans/8.0
            
            return dp[key]
        
        return recurse()
        