class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # top down memoization
        memo = {}
        def recurse(i = n):
            if i == 0 or i == 1: return i
            if i in memo: return memo[i]
            
            memo[i] = recurse(i-1) + recurse(i-2)
            
            return memo[i]
            
        return recurse()
        
#         # bottom up optimized tabulation
#         if n == 0 or n == 1: return n
#         a = 0 
#         b = 1
#         c = 0
        
#         for i in range(2, n + 1):
#             c = a + b
#             a, b = b, c
        
#         return c
        