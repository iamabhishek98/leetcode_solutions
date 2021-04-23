class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        curr = 1
        prev = 0
        for i in range(1,len(s)):
            if s[i]!=s[i-1]:
                prev = curr
                curr = 1
                count += 1
            else:
                curr+=1
                if curr <= prev: count += 1
        return count