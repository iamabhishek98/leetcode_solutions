class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n+1)] for __ in range(m+1)]
        
        # idea is to get the maximum length of the square and then square that number to get the area that square occupies
        max_square_len = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                # we only consider cells which have 1s in them
                if matrix[i-1][j-1] == "1":
                    # all the previous 3 should be at least 1 for the current square length to increase
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + 1
                    # keep track of max at every submatrix
                    max_square_len = max(max_square_len, dp[i][j])
                    
        return max_square_len**2