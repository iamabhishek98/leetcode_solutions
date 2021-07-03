class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        found = False
        count = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] != ' ':    
                count += 1
                found = True
            elif found:
                return count
        return count