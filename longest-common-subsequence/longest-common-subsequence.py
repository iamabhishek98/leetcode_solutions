class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # Method 1: Tabulation (Top down DP approach)
        m = len(text1)
        n = len(text2)
        dp = [[0 for _ in range(n+1)] for __ in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    # current maximum
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    # because it could be matching the previous char
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
        return dp[m][n]
                            