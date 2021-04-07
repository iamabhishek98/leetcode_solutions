class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = n*n
        avg = total/n
        ans = 0
        for i in range(n/2):
            x = (2*i)+1
            ans+=abs(x-avg)
        return ans
            
            
        