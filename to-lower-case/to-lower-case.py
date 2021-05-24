class Solution(object):
    def toLowerCase(self, S):
        """
        :type s: str
        :rtype: str
        """
        s = list(S)
        for i in range(len(s)):
            v = ord(s[i])
            if not 65<=v<=90: continue
            s[i] = chr(v-65+97)
        return "".join(s)