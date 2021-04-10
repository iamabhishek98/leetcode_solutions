class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # right, down, left, up
        d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        count = 0
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = 0
        prev_i = 0
        prev_j = 0
        curr_dir = 0
        arr = []
        while count < m*n:
            if i < 0 or i >= m or j < 0 or j >= n or matrix[i][j] == -101:
                curr_dir += 1
                curr_dir = curr_dir % 4
                i = prev_i
                j = prev_j
            if matrix[i][j] != -101:
                arr.append(matrix[i][j])
                count +=1
            matrix[i][j] = -101
            prev_i = i
            prev_j = j
            i += d[curr_dir][0]
            j += d[curr_dir][1]
            
        return arr