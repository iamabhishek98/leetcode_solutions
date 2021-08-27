class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        def checkSubsequence(a,b):
            # checks if a is subsequence of b
            i = 0
            j = 0
            while i < len(a) and j < len(b):
                if a[i] == b[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
            return i == len(a)
        
        m = -1
        for a in range(len(strs)):
            status = True
            # current string should not be subsequence of any other string 
            for b in range(len(strs)):
                if a != b and checkSubsequence(strs[a],strs[b]):
                    status = False
                    break
            if status:
                m = max(m, len(strs[a]))
        
        return m