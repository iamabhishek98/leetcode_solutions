from collections import Counter

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        m = Counter(s)
        for i in m:
            if m[i]%2==0: ans+=m[i]
            else:ans+=(m[i]-1)
        if ans<len(s): return ans+1
        return ans
