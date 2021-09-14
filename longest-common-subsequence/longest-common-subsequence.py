class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # https://www.youtube.com/watch?v=sSno9rV8Rhg&ab_channel=AbdulBari
        self.dp = {}
        def lcs(i = 0, j = 0):
            if i >= len(text1) or j >= len(text2): return 0
            
            key = tuple([i,j])
            
            if key in self.dp: return self.dp[key]
            
            if text1[i] == text2[j]: 
                return 1 + lcs(i+1,j+1)
            
            self.dp[key] = max(lcs(i+1,j), lcs(i,j+1))
            
            return self.dp[key]
        
        return lcs()
        