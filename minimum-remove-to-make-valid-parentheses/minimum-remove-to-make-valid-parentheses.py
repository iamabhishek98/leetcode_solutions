class Solution(object):
    def minRemoveToMakeValid(self, S):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        s = list(S)
        for i in range(len(s)):
            if (s[i] == "("): stack.append(i)
            elif (s[i] == ")"):
                if stack: stack.pop()
                else: s[i] = ""
        for i in stack:
            s[i] = ""
        return "".join(s)
            
        
        
        