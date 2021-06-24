class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        """
        :type m: int
        :type n: int
        :type maxMove: int
        :type startRow: int
        :type startColumn: int
        :rtype: int
        """
        dp = {}
        
        def dfs(i,j,moveCount):
            key = str(i)+":"+str(j)+":"+str(moveCount)
            
            if key in dp: return dp[key]
            if moveCount > maxMove: return 0
            if i < 0 or i >= m or j < 0 or j >= n: return 1
            
            di = [[1,0],[-1,0],[0,1],[0,-1]]
            count = 0
            for d in di:
                count += dfs(i+d[0],j+d[1],moveCount+1)    
            dp[key] = count
            return dp[key]
        
        return dfs(startRow, startColumn, 0)%(10**9+7)