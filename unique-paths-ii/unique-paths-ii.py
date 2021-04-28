class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        self.dp = [[-1 for i in range(n)] for j in range(m)]
        
        def dfs(i,j):
            if i<m and j<n and self.dp[i][j] != -1: return self.dp[i][j]
            
            if i == m-1 and j == n-1:
                if obstacleGrid[i][j] == 1: return 0
                return 1
            
            if i >= m or j >= n: return 0
            
            if obstacleGrid[i][j]: 
                self.dp[i][j] = 0
                return 0
            
            a = dfs(i+1,j)
            b = dfs(i,j+1)
            res = a+b
            self.dp[i][j] = res
            return res
            
        return dfs(0,0)
