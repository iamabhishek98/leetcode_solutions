class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        if n == 1 or n == 2: return 1
        
        a = 0
        b = c = 1        
        d = 0
        
        for i in range(3, n+1):
            d = a + b + c
            a, b, c = b, c, d
        
        return d