class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # right, down, left, up
        ans = [[0 for i in range(n)] for j in range(n)]        
        visited = [[0 for i in range(n)] for j in range(n)]
        
        d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        count = 1
        i = 0
        j = 0
        prev_i = 0
        prev_j = 0
        curr_dir = 0
        
        while count <= n*n:
            if i < 0 or i >= n or j < 0 or j >= n or visited[i][j] == -1:
                curr_dir += 1
                curr_dir = curr_dir % 4
                i = prev_i
                j = prev_j
            
            if visited[i][j] != -1:
                ans[i][j] = count
                count +=1
            visited[i][j] = -1
            prev_i = i
            prev_j = j
            i += d[curr_dir][0]
            j += d[curr_dir][1]
            
        return ans