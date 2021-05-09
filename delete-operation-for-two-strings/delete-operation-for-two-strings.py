class Solution(object):
    def minDistance(self, text1, text2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        self.dp = [[-1 for i in range(len(text2))] for j in range(len(text1))]
        def lcs(i,j):
            if i >= len(text1) or j >= len(text2): return 0
            if self.dp[i][j] != -1: return self.dp[i][j]
            if text1[i] == text2[j]: return 1 + lcs(i+1,j+1)
            self.dp[i][j] = max(lcs(i+1,j),lcs(i,j+1))
            return self.dp[i][j]
        l = lcs(0,0)
        return len(text1)-l+len(text2)-l
        