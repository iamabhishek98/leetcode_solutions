def check(s,words):
    for i in range(1,len(s)):
        if s[0:i] not in words: return False
    return True
    
class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        ans = ""
        for i in words:
            if len(i) >= len(ans) and check(i,words):
                if len(i) == len(ans) and i > ans: continue
                ans = i
        return ans

                
        