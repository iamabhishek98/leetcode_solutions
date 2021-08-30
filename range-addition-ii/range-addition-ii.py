class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops: return m*n
        
        min_a = sys.maxint
        min_b = sys.maxint
        
        for op in ops:
            min_a = min(min_a, op[0])
            min_b = min(min_b, op[1])
        
        return min_a*min_b
        