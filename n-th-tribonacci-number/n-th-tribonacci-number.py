class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        seq = [0]*38
        seq[1] = seq[2] = 1
        
        for i in range(3, n+1):
            seq[i] = seq[i-1]+seq[i-2]+seq[i-3]
        
        return seq[n]