class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {}
        for i,x in enumerate(s):
            if x in m: m[x] = -1
            else: m[x] = i
        
        smallest = sys.maxint
        for key in m:
            if m[key] != -1:
                smallest = min(smallest,m[key])
        
        return -1 if smallest == sys.maxint else smallest