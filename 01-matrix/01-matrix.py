class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        dist = [[sys.maxint for i in range(len(matrix[0]))] for j in range(len(matrix))]
            
        q = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    q.append([i,j])
                    dist[i][j] = 0
        
        while len(q):
            v = q.pop(0)
            oi = v[0]
            oj = v[1]
            
            for i in range(4):
                ni = d[i][0]+oi
                nj = d[i][1]+oj
                if ni >= 0 and ni < len(matrix) and nj >= 0 and nj < len(matrix[0]):
                    if dist[ni][nj] > dist[oi][oj]+1:
                        dist[ni][nj] = dist[oi][oj]+1
                        q.append([ni,nj])
        
        return dist
        