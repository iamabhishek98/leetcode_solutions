from collections import Counter

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        grp = {}
        
        for s in strs:
            m = Counter(s)
            key = ""
            for i in sorted(m.keys()):
                key += i + str(m[i])
            if key not in grp: grp[key] = [s]
            else: grp[key].append(s)
        
        return grp.values()