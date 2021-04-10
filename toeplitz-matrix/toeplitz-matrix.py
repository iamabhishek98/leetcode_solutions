class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        def check(i,j,prev_i,prev_j):
            while i < len(matrix) and j < len(matrix[0]):
                if matrix[i][j] != matrix[prev_i][prev_j]: return False
                prev_i = i
                prev_j = j
                i+=1
                j+=1
            return True
        
        for i in range(len(matrix)):
            prev_i = i
            j = prev_j = 0
            if not check(i,j,prev_i,prev_j): return False        

        
        for j in range(len(matrix[0])):
            prev_i = i = 0
            prev_j = j
            if not check(i,j,prev_i,prev_j): return False        
            
        return True
        