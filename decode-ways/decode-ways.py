class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = {}
        
        def recurse(i = 0):
            if i in dp: return dp[i]
            
            if i == len(s): return 1
            
            count = 0
            
            # if it is one digit, it cannot be equal to 0 as 0 does not map to any character
            if s[i] != "0":
                count += recurse(i+1)            
            
            # if it is double digit, it should be between 10 and 26
            if i+1 < len(s) and (s[i] == "1" or (s[i] == "2" and ord(s[i+1]) <= ord('6'))):
                count += recurse(i+2)
            
            dp[i] = count
            return count
            
        return recurse()
