class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n = len(grid[0])
        m = len(grid)
        self.visited = [[0 for i in range(n)] for j in range(m)]
        def dfs(i,j,m,n):
            if i<0 or i >= m or j <0 or j >= n or self.visited[i][j] or grid[i][j] == "0": return
            self.visited[i][j] = 1
            dir = [[-1,0],[0,-1],[1,0],[0,1]]
            for x in dir:
                dfs(i+x[0],j+x[1],m,n)
            
        count = 0
        for i,x in enumerate(grid):
            for j,y in enumerate(grid[0]):
                if  grid[i][j] == "1" and not self.visited[i][j]:
                    dfs(i,j,m,n)
                    count += 1
        return count