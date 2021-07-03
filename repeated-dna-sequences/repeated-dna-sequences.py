from collections import Counter

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s)<10: return []
        
        occurrences = {}
        i = 0        
        currentMap = Counter(s[i:i+10])
        while i+10 <= len(s):
            currStr = s[i:i+10]
            if currStr not in occurrences: occurrences[currStr] = 1
            else: occurrences[currStr]+=1 
            i+=1

        ans = []
        for i in occurrences:
            if occurrences[i]>1: ans.append(i)
        
        return ans