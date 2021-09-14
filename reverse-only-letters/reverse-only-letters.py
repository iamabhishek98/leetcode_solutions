class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type s: str
        :rtype: str
        """
        s = list(S)
        i = 0
        j = len(s) - 1

        while i < j:
            if not (0 <= ord(s[i]) - ord('a') < 26 or 0 <= ord(s[i]) - ord('A') < 26):
                i += 1
                continue
            if not (0 <= ord(s[j]) - ord('a') < 26 or 0 <= ord(s[j]) - ord('A') < 26):
                j -= 1
                continue
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        
        return "".join(s)
        
            