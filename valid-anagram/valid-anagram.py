from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False
        
        l1 = Counter(s)
        l2 = Counter(t)
        
        for key in l1:
            if key not in l2 or l1[key] != l2[key]: return False
        
        for key in l2:
            if key not in l1 or l2[key] != l1[key]: return False
        
        return True