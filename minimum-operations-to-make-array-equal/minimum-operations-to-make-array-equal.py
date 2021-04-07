class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        for i in range(n/2):
            x = (2*i)+1
            ans+=abs(x-n)
        return ans
            
            
        