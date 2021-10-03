class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # Tabulation (bottom up iterative dp approach)
        
        # https://www.youtube.com/watch?v=MiqoA-yF-0M&ab_channel=BackToBackSWE
        # the idea is to break down this into subproblems involving substrings of the 2 words
        
        m = len(word1)
        n = len(word2)
        
        # each cell in the table represents the min edit distance to the substrings
        dp = [[0 for _ in range(n+1)] for __ in range(m+1)]
        
        # the cell [0,0] indicates that no changes need to be made because it represents an empty string
        # the table first row and fist column contains the indexes of all the characters
        # the reason for this is because this signifies the min edit distance from an empty string to that substring 
        # this makes sense because to change an empty string to a substring, that many characters need to be added
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
                
                # at every cell we know that the top, left and diagonally previous cell 
                # already contains the minimum distance to that previous particular substring
                # so we need to take the minimum of all the 3 operations accounting for this
                
                # the col to the left means you want to delete the current character in word1 
                # and then add the new character from word2 to the prev corresponding substring
                delete = dp[i-1][j] + 1
                
                # the row to the top means you want to delete the current character in word2
                # and then add the new character from word1 to the prev corresponding substring
                insert = dp[i][j-1] + 1
                
                # the previous substring without the current characters in word 1 and word2 
                # added to the current cost of replacement
                replace = dp[i-1][j-1] + cost
                
                dp[i][j] = min(insert,delete,replace)
        
        return dp[m][n]