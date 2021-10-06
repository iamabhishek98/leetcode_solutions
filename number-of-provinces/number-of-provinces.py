class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        visited = [0 for __ in range(n)]
        
        def dfs(i):
            for j in range(n):
                if isConnected[i][j] and not visited[j]:
                    visited[j] = 1
                    dfs(j)
        
        count = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1

        return count