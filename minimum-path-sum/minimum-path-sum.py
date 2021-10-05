class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        
        dp = {}
        def recurse(i=0, j=0):
            if i >= m or j >= n:
                # returning max int because we want minimum
                return sys.maxint
            
            key = (i,j)
            if key in dp: return dp[key]
            
            if i == m-1 and j == n-1:
                return grid[i][j]
            
            # down or right
            dp[key] = min(grid[i][j]+recurse(i+1,j),grid[i][j]+recurse(i,j+1))
            
            return dp[key]
        
        return recurse()