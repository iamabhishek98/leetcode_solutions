

class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(matrix)==0: return []
        self.matrix = matrix
        
        
        def dfs(visited,i,j,m,n):
            visited[i][j] = True
            if i-1>=0 and not visited[i-1][j] and self.matrix[i-1][j] >= self.matrix[i][j]:
                dfs(visited,i-1,j,m,n)
            if j-1>=0 and not visited[i][j-1] and self.matrix[i][j-1] >= self.matrix[i][j]:
                dfs(visited,i,j-1,m,n)
            if i+1<m and not visited[i+1][j] and self.matrix[i+1][j] >= self.matrix[i][j]:
                dfs(visited,i+1,j,m,n)
            if j+1<n and not visited[i][j+1] and self.matrix[i][j+1] >= self.matrix[i][j]:
                dfs(visited,i,j+1,m,n)
        
        pacific = [[False for a in range(len(matrix[0]))] for b in range(len(matrix))]
        atlantic = [[False for c in range(len(matrix[0]))] for d in range(len(matrix))]
        for i in range(len(matrix)):
            dfs(pacific,i,0,len(matrix),len(matrix[0]))
            dfs(atlantic,i,len(matrix[0])-1,len(matrix),len(matrix[0]))
        for j in range(len(matrix[0])):
            dfs(pacific,0,j,len(matrix),len(matrix[0]))
            dfs(atlantic,len(matrix)-1,j,len(matrix),len(matrix[0]))
        
        ans = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if pacific[i][j] and atlantic[i][j]:
                    ans.append([i,j])
        
        return ans