from collections import Counter

class Solution(object):
    def canReorderDoubled(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        c = Counter(arr)
        for key in sorted(c.keys()):
            if c[key] > 0:
                if key == 0 and c[key]%2 != 0: return False
                elif key > 0:
                    if 2*key not in c or (2*key in c and c[key] > c[2*key]):
                        return False
                    c[2*key] -= c[key]
                else:
                    if key/float(2) not in c or (key/float(2) in c and c[key] > c[key/float(2)]):
                        return False
                    c[key/float(2)] -= c[key]
        
        return True
        
        