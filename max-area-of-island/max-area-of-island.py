class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        self.visited = [[0 for a in range(n)] for b in range(m)]
        def dfs(i,j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0 or self.visited[i][j]: return 0
            self.visited[i][j] = 1
            curr = 1 
            dir = [[0,1],[0,-1],[1,0],[-1,0]]
            for x in dir:
                curr+= dfs(i+x[0],j+x[1])
            return curr
        
        max_v = 0
        for i in range(m):
            for j in range(n):
                max_v = max(max_v, dfs(i,j))   
        return max_v