class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        
        dp = [[0 for _ in range(n+1)] for __ in range(m+1)]
        
        # the table first row and column contains the indexes of all the characters
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
                
        for i in range(1,m+1):
            for j in range(1,n+1):
                # if the characters are equal there is no need to replace anything
                cost = 0
                # if the characters are different, then we need to replace the character
                if word1[i-1] != word2[j-1]:
                    cost = 1
                
                # take min of all 3 operations
                delete = dp[i-1][j] + 1
                insert = dp[i][j-1] + 1
                replace = dp[i-1][j-1] + cost
                dp[i][j] = min(insert,delete,replace)
        
        return dp[m][n]