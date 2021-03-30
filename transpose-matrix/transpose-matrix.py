class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not len(matrix): return matrix
        m = len(matrix)
        n = len(matrix[0])
        new_matrix = [[0 for i in range(m)] for j in range(n)]
        print new_matrix
        for i in range(m):
            for j in range(n):
                new_matrix[j][i] = matrix[i][j]
        return new_matrix
        