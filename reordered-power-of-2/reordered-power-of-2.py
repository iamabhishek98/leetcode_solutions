import itertools

class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        s = set()
        for i in range(30):
            s.add(str(pow(2,i)))
        l = list(str(N))
        per = list(itertools.permutations(l))
        for i in per:
            if ''.join(i) in s:
                return True
        return False
        
        